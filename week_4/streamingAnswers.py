import os
from collections.abc import AsyncIterable
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.sse import EventSourceResponse, ServerSentEvent
from openai import APIError, AsyncOpenAI

# The keys live in claude-quickstart/.env, one folder below this script
load_dotenv(Path(__file__).parent / "claude-quickstart" / ".env")

# AsyncOpenAI, not OpenAI: while this endpoint waits for the next token it must hand the
# event loop back to the server, or one long answer would freeze every other request.
# Gemini is out of prepaid credits, so this uses Groq through its OpenAI-compatible API.
client = AsyncOpenAI(
    api_key=os.environ["GROK_API_KEY"],
    base_url="https://api.groq.com/openai/v1",
)

MODEL = "openai/gpt-oss-120b"

app = FastAPI()


# response_class=EventSourceResponse plus `yield` is FastAPI's built-in SSE support.
# FastAPI sets Content-Type: text/event-stream, writes each ServerSentEvent as
# "event:" / "data:" lines ending in a blank line, and sends a ": ping" comment
# after 15 seconds of silence so proxies don't drop the idle connection.
# It is a GET because the browser's EventSource can only send GET requests.
@app.get("/chat", response_class=EventSourceResponse)
async def chat(question: str) -> AsyncIterable[ServerSentEvent]:
    try:
        stream = await client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": question}],
            reasoning_effort="low",  # gpt-oss thinks before answering; less thinking = first word sooner
            stream=True,  # get the answer as small chunks while it is written, not one message at the end
        )
        # `async with` closes the Groq connection if the client hangs up mid-answer,
        # so we stop generating (and paying for) tokens nobody will read
        async with stream:
            async for chunk in stream:
                if not chunk.choices:
                    continue
                choice = chunk.choices[0]

                # The first chunk carries only the role and the last only finish_reason, so content can be empty
                if choice.delta.content:
                    # data is JSON-encoded, so a token containing "\n" can't end the event early
                    yield ServerSentEvent(data={"text": choice.delta.content})

                if choice.finish_reason:
                    # Tell the client the answer is complete. Without this, the browser's EventSource
                    # treats the closed connection as a dropped one and reconnects, asking the question again.
                    yield ServerSentEvent(event="done", data={"finish_reason": choice.finish_reason})
    except APIError as e:
        # The 200 status went out when the stream opened, so a failure can't become a 500 any more.
        # Send it as an event instead so the client can show it.
        yield ServerSentEvent(event="error", data={"message": e.message})
