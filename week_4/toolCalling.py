import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# The Windows console defaults to cp1252, which can't print characters like the model's non-breaking hyphens
sys.stdout.reconfigure(encoding="utf-8")

# The keys live in claude-quickstart/.env, one folder below this script
load_dotenv(Path(__file__).parent / "claude-quickstart" / ".env")

# Gemini is out of prepaid credits, so this uses Groq through its OpenAI-compatible API.
# Loop follows https://console.groq.com/docs/tool-use/local-tool-calling
client = OpenAI(
    api_key=os.environ["GROK_API_KEY"],
    base_url="https://api.groq.com/openai/v1",
)

MODEL = "openai/gpt-oss-120b"
MAX_TURNS = 10  # guard against a model that keeps calling tools forever

# Fake data keeps the focus on the loop; a real version would call a weather API here
FAKE_WEATHER = {
    "bengaluru": {"temp_c": 24, "conditions": "light rain"},
    "london": {"temp_c": 11, "conditions": "overcast"},
    "tokyo": {"temp_c": 18, "conditions": "sunny"},
}


def get_weather(city: str) -> dict:
    weather = FAKE_WEATHER.get(city.strip().lower())
    if weather is None:
        # Hand the error back to the model instead of crashing, so it can tell the user
        return {"error": f"No weather data for {city}"}
    return {"city": city, **weather}


# Step 1: describe the function to the model. The model only sees this description,
# never the Python code, so the description is what decides when it gets called.
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather for a city. Use it whenever the user asks about weather, temperature or what to wear.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name, for example London"},
                },
                "required": ["city"],
            },
        },
    }
]

# Maps the tool name the model asks for to the Python function we actually run
AVAILABLE_FUNCTIONS = {"get_weather": get_weather}


def ask(question: str) -> str:
    messages = [
        {"role": "system", "content": "You are a helpful assistant. Use tools for weather facts instead of guessing."},
        {"role": "user", "content": question},
    ]

    for _ in range(MAX_TURNS):
        # Step 2: send the conversation plus the tool list. tool_choice="auto" lets the model decide.
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            temperature=0,
        )
        message = response.choices[0].message

        # Step 5: no tool calls means the model is done and this is the final answer
        if not message.tool_calls:
            return message.content

        # Step 3: keep the model's tool request in the history, before the results
        messages.append(message)

        # Step 4: run every requested call and send each result back, matched by tool_call_id
        for tool_call in message.tool_calls:
            name = tool_call.function.name
            args = json.loads(tool_call.function.arguments)  # arguments arrive as a JSON string
            print(f"  -> model called {name}({args})")

            function = AVAILABLE_FUNCTIONS.get(name)
            result = function(**args) if function else {"error": f"Unknown tool {name}"}
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": name,
                "content": json.dumps(result),
            })

    raise RuntimeError(f"No final answer after {MAX_TURNS} turns")


QUESTIONS = [
    "Should I carry an umbrella in Bengaluru today? What about London?",
    "What is the capital of France?",  # no weather needed, so the model should skip the tool
    "How warm is it in Atlantis right now?",  # unknown city, exercises the error path
]

for question in QUESTIONS:
    print(f"\nQ: {question}")
    print(f"A: {ask(question)}")
