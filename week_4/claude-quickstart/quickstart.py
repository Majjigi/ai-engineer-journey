from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()

SYSTEM_PROMPT = """You are a strict Angular code reviewer.
Review against current Angular best practices: standalone components, signals,
OnPush change detection, typed reactive forms, no memory leaks from unmanaged
subscriptions, and no logic in templates.
For each issue, give the line, why it's a problem, and the fix. Flag severity
as blocker, major or minor. If the code is fine, say so briefly."""

stream = client.interactions.create(
    model="gemini-2.5-flash",
    system_instruction=SYSTEM_PROMPT,
    input="Explain how AI works",
    generation_config={"temperature": 0.2},
    stream=True
)

for event in stream:
    if event.event_type == "step.delta" and event.delta.type == "text":
        print(event.delta.text, end="", flush=True)
print()