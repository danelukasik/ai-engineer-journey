from dotenv import load_dotenv
import os
import anthropic

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

messages = [
    {"role": "user", "content": "My name is Dane. What's 12 * 7?"}
]

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=200,
    messages=messages
)
print(response.content[0].text)

# Now ask a follow-up that depends on remembering context
messages.append({"role": "assistant", "content": response.content[0].text})
messages.append({"role": "user", "content": "What's my name?"})

response2 = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=200,
    messages=messages
)
print(response2.content[0].text)