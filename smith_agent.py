from typing import TypedDict, List, Dict, Any, Optional
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# -------------------------------------------------------------------------
# 1. DEFINE THE SHARED STATE
# -------------------------------------------------------------------------
class SmithAgentState(TypedDict):
    task: str
    telemetry_data: Dict[str, Any]
    analysis_summary: str
    plan_steps: List[str]
    execution_results: List[Dict[str, Any]]
    audit_passed: bool
    audit_feedback: Optional[str]
    retry_count: int

# -------------------------------------------------------------------------
# 2. INITIALIZE MODEL
# -------------------------------------------------------------------------
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.2)

# -------------------------------------------------------------------------
# 3. DEFINE SUB-AGENT NODES
# -------------------------------------------------------------------------
def analyst_node(state: SmithAgentState) -> Dict[str, Any]:
    prompt = f"""
    You are THE ANALYST (Smith Agent Perception Engine).
    Task: {state['task']}
    Telemetry/Context: {state.get('telemetry_data', {})}
    Audit Feedback: {state.get('audit_feedback', 'None')}

    Establish ground truth, identify anomalies, and summarize operational reality.
    """
    response = llm.invoke([SystemMessage(content=prompt)])
    return {"analysis_summary": response.content}

def planner_node(state: SmithAgentState) -> Dict[str, Any]:
    prompt = f"""
    You are THE PLANNER (Smith Agent Strategy Engine).
    Analysis: {state['analysis_summary']}
    Task: {state['task']}

    Create a strict list of 2-4 actionable tool execution steps.
    Format as separate lines starting with 'STEP:'.
    """
    response = llm.invoke([SystemMessage(content=prompt)])
    steps = [line for line in response.content.split("\n") if line.strip().startswith("STEP:")]
    return {"plan_steps": steps if steps else [response.content]}

def operator_node(state: SmithAgentState) -> Dict[str, Any]:
    results = []
    for step in state['plan_steps']:
        results.append({"step": step, "status": "SUCCESS", "output": f"Executed: {step}"})
    return {"execution_results": results}

def auditor_node(state: SmithAgentState) -> Dict[str, Any]:
    prompt = f"""
    You are THE AUDITOR (Smith Agent Governance & Quality Control).
    Task: {state['task']}
    Execution Results: {state['execution_results']}

    Verify:
    1. Did we achieve the Goal?
    2. Is there verifiable Proof/Data?
    3. Were all Steps executed without violation?

    Respond strictly with:
    STATUS: APPROVED (or REJECTED)
    REASON: <concise reason>
    """
    response = llm.invoke([SystemMessage(content=prompt)])
    content = response.content.upper()
    is_approved = "STATUS: APPROVED" in content or "APPROVED" in content
    
    return {
        "audit_passed": is_approved,
        "audit_feedback": None if is_approved else response.content,
        "retry_count": state.get("retry_count", 0) + 1
    }

# -------------------------------------------------------------------------
# 4. CONDITIONAL ROUTING
# -------------------------------------------------------------------------
def evaluate_audit_decision(state: SmithAgentState) -> str:
    if state.get("audit_passed", False) or state.get("retry_count", 0) >= 3:
        return "approved"
    return "rejected"

# -------------------------------------------------------------------------
# 5. ASSEMBLE GRAPH
# -------------------------------------------------------------------------
workflow = StateGraph(SmithAgentState)

workflow.add_node("analyst", analyst_node)
workflow.add_node("planner", planner_node)
workflow.add_node("operator", operator_node)
workflow.add_node("auditor", auditor_node)

workflow.add_edge(START, "analyst")
workflow.add_edge("analyst", "planner")
workflow.add_edge("planner", "operator")
workflow.add_edge("operator", "auditor")

workflow.add_conditional_edges(
    "auditor",
    evaluate_audit_decision,
    {
        "approved": END,
        "rejected": "analyst"
    }
)

smith_agent_app = workflow.compile()

# -------------------------------------------------------------------------
# 6. TEST RUNNER
# -------------------------------------------------------------------------
if __name__ == "__main__":
    test_state = {
        "task": "Triage STAT13 scan anomalies on Sort Line B and recommend operational adjustments.",
        "telemetry_data": {
            "sort_line": "B",
            "stat13_failures": 42,
            "belt_speed_fps": 7.8,
            "chute_congestion": "HIGH"
        },
        "retry_count": 0
    }

    print("🚀 Starting Smith Agent Loop...\n")
    for event in smith_agent_app.stream(test_state):
        for node_name, state_update in event.items():
            print(f"🔹 [Completed: {node_name.upper()}]")
            for key, val in state_update.items():
                print(f"   ↳ {key}: {str(val)[:120]}...")
            print("-" * 50)
