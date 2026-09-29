from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from typing import TypedDict, Annotated
import operator
import anthropic
from dotenv import load_dotenv
import os

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]

def call_model(state: AgentState) -> AgentState:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        messages=state["messages"]
    )
    # Convert SDK objects to plain dicts before they ever touch checkpointed state
    content = [block.model_dump() for block in response.content]
    return {"messages": [{"role": "assistant", "content": content}]}

graph = StateGraph(AgentState)
graph.add_node("agent", call_model)
graph.set_entry_point("agent")
graph.add_edge("agent", END)

memory = MemorySaver() 
app = graph.compile(checkpointer=memory)

config = {"configurable": {"thread_id": "conversation-1"}}

result1 = app.invoke(
    {"messages": [{"role": "user", "content": "My name is Dane."}]},
    config=config
)
print(result1["messages"][-1]["content"][0]["text"])

# Separate invoke with same thread_id to retrieve memory
result2 = app.invoke(
    {"messages": [{"role": "user", "content": "What's my name?"}]},
    config=config
)
print(result2["messages"][-1]["content"][0]["text"])

# Separate invoke with different thread_id to prove different memory
result3 = app.invoke(
    {"messages": [{"role": "user", "content": "What's my name?"}]},
    config={"configurable": {"thread_id": "conversation-2"}}
)
print(result3["messages"][-1]["content"][0]["text"])