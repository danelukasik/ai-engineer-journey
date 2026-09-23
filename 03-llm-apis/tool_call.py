from dotenv import load_dotenv
import os
import anthropic

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

tools = [
    {
        "name": "add_numbers",
        "description": "Adds two numbers together and returns the sum.",
        "input_schema": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "The first number"},
                "b": {"type": "number", "description": "The second number"}
            },
            "required": ["a", "b"]
        }
    },
    {
        "name": "subtract_numbers",
        "description": "Subtracts the second number from the first and returns the difference.",
        "input_schema": {
            "type": "object",
            "properties": {
                "a": {"type": "number", "description": "The first number"},
                "b": {"type": "number", "description": "The second number"}
            },
            "required": ["a", "b"]
        }
    }
]

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=500,
    tools=tools,
    messages=[
        {"role": "user", "content": "What's 47 minus 89?"}
    ]
)

print(response.stop_reason)  # should print "tool_use"
for block in response.content:
    print(block)

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

tool_functions = {
    "add_numbers": add_numbers,
    "subtract_numbers": subtract_numbers
}

# Find the tool_use block
tool_use_block = next(block for block in response.content if block.type == "tool_use")

# Actually run the function with the model's chosen arguments
function_to_call = tool_functions[tool_use_block.name]
result = function_to_call(**tool_use_block.input)

# Send the result back so the model can respond to the user
follow_up = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=500,
    tools=tools,
    messages=[
        {"role": "user", "content": "What's 47 minus 89?"},
        {"role": "assistant", "content": response.content},
        {"role": "user", "content": [
            {"type": "tool_result", "tool_use_id": tool_use_block.id, "content": str(result)}
        ]}
    ]
)

print(follow_up.content[0].text)