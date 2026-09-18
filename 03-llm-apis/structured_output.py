from dotenv import load_dotenv
import os
import anthropic

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

extraction_tool = [
    {
        "name": "extract_customer_info",
        "description": "Extracts structured customer information from a message.",
        "input_schema": {
            "type": "object",
            "properties": {
                "name": {"type": "string", "description": "The customer's name"},
                "issue_category": {
                    "type": "string",
                    "enum": ["billing", "technical", "shipping", "other"],
                    "description": "What kind of issue this is"
                },
                "urgency": {
                    "type": "string",
                    "enum": ["low", "medium", "high"],
                    "description": "How urgent the issue seems"
                }
            },
            "required": ["name", "issue_category", "urgency"]
        }
    }
]

messages_list = ["Hi, this is Sarah Chen. My package was supposed to arrive 3 days ago and I need it TODAY for an event.",
                 "Hello, I'm John Doe. I was charged twice for my last order and need a refund.",
                 "Hey, this is Emily. I can't log into my account and need help resetting my password.",
                 "Hi, I'm Michael. I received the wrong item in my order and need to exchange it ASAP.",
                 "Hello, this is Jessica. I have a question about the warranty on my product."]

import pandas as pd

results = []
for message in messages_list:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=300,
        tools=extraction_tool,
        tool_choice={"type": "tool", "name": "extract_customer_info"},  # forces this exact tool, every time
        messages=[
            {"role": "user", "content": message}
        ]
    )
    tool_use_block = next(block for block in response.content if block.type == "tool_use")
    results.append(tool_use_block.input)

df = pd.DataFrame(results)
print(df)