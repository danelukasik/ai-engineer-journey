from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from typing import TypedDict, Annotated
import operator

class AgentState(TypedDict):
    messages: Annotated[list, operator.add]
    action: str

def propose_action(state: AgentState) -> AgentState:
    # Pretend this decided to do something real, like "delete_customer_record"
    return {"action": "DELETE customer_id=42 FROM database"}

def execute_action(state: AgentState) -> AgentState:
    print(f"Executing: {state['action']}")
    return {"messages": [{"role": "assistant", "content": f"Done: {state['action']}"}]}

graph = StateGraph(AgentState)
graph.add_node("propose", propose_action)
graph.add_node("execute", execute_action)
graph.set_entry_point("propose")
graph.add_edge("propose", "execute")
graph.add_edge("execute", END)

memory = MemorySaver()
app = graph.compile(checkpointer=memory, interrupt_before=["execute"]) 

config = {"configurable": {"thread_id": "approval-1"}}

# Step 1: run up to the interrupt point
result = app.invoke({"messages": [], "action": ""}, config=config)
print("Paused. Proposed action:", result["action"])

# Step 2: human approval or decline
user_approval = input("Approve this action? (yes/no): ")

if user_approval.lower() == "yes":
    # Step 3: resume execution after approval
    final_result = app.invoke(None, config=config)
    print(final_result["messages"][-1]["content"])
else:
    print("Action cancelled.")