from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
import operator
import anthropic
from dotenv import load_dotenv
import os

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]

tools = [
    {
        "name": "add_numbers",
        "description": "Adds two numbers together and returns the sum.",
        "input_schema": {
            "type": "object",
            "properties": {"a": {"type": "number"}, "b": {"type": "number"}},
            "required": ["a", "b"]
        }
    },
    {
        "name": "subtract_numbers",
        "description": "Subtracts the second number from the first.",
        "input_schema": {
            "type": "object",
            "properties": {"a": {"type": "number"}, "b": {"type": "number"}},
            "required": ["a", "b"]
        }
    }
]

def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

tool_functions = {"add_numbers": add_numbers, "subtract_numbers": subtract_numbers}

# NODE 1: Call Claude
def call_model(state: AgentState) -> AgentState:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        tools=tools,
        messages=state["messages"]
    )
    # Convert SDK objects to plain dicts before they ever touch checkpointed state
    content = [block.model_dump() for block in response.content]
    return {"messages": [{"role": "assistant", "content": content}]}

# NODE 2: Run whatever tool Claude asked for
def call_tool(state: AgentState) -> AgentState:
    last_message = state["messages"][-1]
    tool_use_blocks = [block for block in last_message["content"] if block["type"] == "tool_use"]

    tool_results = []
    for tool_use_block in tool_use_blocks:
        function_to_call = tool_functions[tool_use_block["name"]]
        result = function_to_call(**tool_use_block["input"])
        tool_results.append({
            "type": "tool_result",
            "tool_use_id": tool_use_block["id"],
            "content": str(result)
        })

    return {"messages": [{"role": "user", "content": tool_results}]}

def should_continue(state: AgentState) -> str:
    last_message = state["messages"][-1]
    for block in last_message["content"]:
        if block["type"] == "tool_use":
            return "use_tool"
    return "done"

graph = StateGraph(AgentState)
graph.add_node("agent", call_model)
graph.add_node("tools", call_tool)

graph.set_entry_point("agent")

graph.add_conditional_edges(
    "agent",
    should_continue,
    {"use_tool": "tools", "done": END}
)
graph.add_edge("tools", "agent")  # THE LOOP: after running a tool, go back to the agent to respond

app = graph.compile()

result = app.invoke({"messages": [{"role": "user", "content": "What's 47 plus 89, and what's 100 minus 37?"}]})

for message in result["messages"]:
    print(message)
    print("---")