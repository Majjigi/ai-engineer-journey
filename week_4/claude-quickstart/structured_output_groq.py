import os

from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel, ConfigDict, Field, ValidationError

load_dotenv()

# Groq speaks the OpenAI API, so the OpenAI SDK works with a different base_url.
# The key in .env starts with gsk_, which makes it a Groq key (not xAI Grok).
client = OpenAI(
    api_key=os.environ["GROK_API_KEY"],
    base_url="https://api.groq.com/openai/v1",
)


class JobPosting(BaseModel):
    # Strict mode needs additionalProperties: false, which extra="forbid" adds to the schema
    model_config = ConfigDict(extra="forbid")

    company: str | None = Field(description="Hiring company's name, or null if the posting doesn't name it")
    role: str = Field(description="Job title exactly as written in the posting")
    skills: list[str] = Field(description="Each required or preferred skill as a short noun phrase")
    experience: str | None = Field(description="Experience level required for the role, or null if not specified")


# Prompt elements from the Prompt Engineering Guide:
# instruction first, ### separators around the input, specific wording,
# and the output indicator is the JSON schema passed in response_format.
SYSTEM_PROMPT = """You extract structured data from job descriptions.
Use only facts stated in the posting. Write each skill as a short noun phrase,
for example "Python", "Kubernetes" or "stakeholder communication", and list
each skill once. If the posting doesn't name the company, set company to null."""

JOB_DESCRIPTION = """Senior Backend Engineer - Payments
Northwind Labs is hiring a Senior Backend Engineer to scale our payments platform.
You'll design REST and gRPC services in Go and Python, run them on Kubernetes in AWS,
and own PostgreSQL schemas for ledger data. We expect 5+ years of backend experience,
strong knowledge of distributed systems, and clear written communication.
Nice to have: Kafka, Terraform, and PCI-DSS compliance experience."""

completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": f"Extract the company, role and skills from this job description.\n\n###\n{JOB_DESCRIPTION}\n###",
        },
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "job_posting",
            "strict": True,
            "schema": JobPosting.model_json_schema(),
        },
    },
    temperature=0,
)

raw = completion.choices[0].message.content
print("Raw model output:")
print(raw)

try:
    job = JobPosting.model_validate_json(raw)
except ValidationError as e:
    print("\nOutput does NOT match the JobPosting schema:")
    print(e)
    raise SystemExit(1)

print("\nValidated JobPosting:")
print(job.model_dump_json(indent=2))
