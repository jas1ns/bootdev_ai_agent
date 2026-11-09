import argparse
import os
from dotenv import load_dotenv
from openai import OpenAI

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()


load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key is None:
    raise ValueError("OPENROUTER_API_KEY environment variable not found")

client = OpenAI(api_key=api_key, base_url="https://openrouter.ai/api/v1")

response = client.chat.completions.create(
    model="openrouter/free",
    messages=[
        {
            "role": "user",
            "content": args.user_prompt,
        }
    ],
)

if response.usage is None:
    raise RuntimeError("Usage information is missing from the response")
else:
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")
    print(f"Response: {response.choices[0].message.content}")