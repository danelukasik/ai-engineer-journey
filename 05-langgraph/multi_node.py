from langgraph.graph import StateGraph, END
from typing import TypedDict

class AgentState(TypedDict):
    message: str
    word_count: int
    response: str

def count_words(state: AgentState) -> AgentState:
    count = len(state["message"].split())
    return {"word_count": count}

def handle_short_message(state: AgentState) -> AgentState:
    return {"response": "That was brief! Say more?"}

def handle_long_message(state: AgentState) -> AgentState:
    return {"response": f"That's a {state['word_count']}-word message — thorough!"}

def route_by_length(state: AgentState) -> str:
    if state["word_count"] < 5:
        return "short"
    else:
        return "long"

graph = StateGraph(AgentState)
graph.add_node("counter", count_words)
graph.add_node("short_handler", handle_short_message)
graph.add_node("long_handler", handle_long_message)

graph.set_entry_point("counter")

graph.add_conditional_edges(
    "counter",           # after this node runs...
    route_by_length,      # ...call this function to decide where to go next...
    {
        "short": "short_handler",   # if route_by_length returns "short", go here
        "long": "long_handler"      # if it returns "long", go here instead
    }
)

graph.add_edge("short_handler", END)
graph.add_edge("long_handler", END)

app = graph.compile()

result1 = app.invoke({"message": "Hi there", "word_count": 0, "response": ""})
print(result1)

result2 = app.invoke({"message": "This is a much longer test sentence with many words", "word_count": 0, "response": ""})
print(result2)