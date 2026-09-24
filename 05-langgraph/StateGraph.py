from langgraph.graph import StateGraph, END
from typing import TypedDict

class AgentState(TypedDict):
    message: str
    word_count: int

def count_words(state: AgentState) -> AgentState:
    count = len(state["message"].split())
    return {"word_count": count}

# Build the graph
graph = StateGraph(AgentState)
graph.add_node("counter", count_words)
graph.set_entry_point("counter")
graph.add_edge("counter", END)

app = graph.compile()

result = app.invoke({"message": "This is a test sentence", "word_count": 0})
print(result)