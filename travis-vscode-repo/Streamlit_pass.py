import streamlit as st
import os

# Import your Smith Agent compiled graph (or ChatVertexAI / ChatGoogleGenerativeAI directly)
try:
    from smith_agent import smith_agent_app
    HAS_AGENT = True
except ImportError:
    HAS_AGENT = False
    from langchain_google_genai import ChatGoogleGenerativeAI
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.2)

# --- 1. PAGE SETUP ---
st.set_page_config(page_title="Smith Agent Operations", page_icon="🤖", layout="centered")
st.title("🤖 Smith Agent: Operational Assistant")
st.caption("Ask questions about station metrics, compliance certs, scan anomalies, or drafting communications.")

# --- 2. INITIALIZE SESSION STATE (Chat Memory) ---
# This prevents Streamlit from wiping out history or re-running answers from top to bottom
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello Travis! I am the Smith Agent mastermind. What operational task or station data can I help you investigate today?"}
    ]

# --- 3. RENDER PAST CONVERSATION ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- 4. CAPTURE USER QUERY DYNAMICALLY ---
# This only triggers when the user types a question and hits Enter
if user_query := st.chat_input("Ask a question (e.g., 'Pull Switcher certs for station 342')..."):
    
    # 1. Display user query immediately
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    # 2. Process query with the Agent
    with st.chat_message("assistant"):
        with st.spinner("Smith Agent analyzing objective..."):
            
            if HAS_AGENT:
                # Pass the EXACT user question into the Smith Agent 4-role loop
                initial_state = {
                    "task": user_query,
                    "telemetry_data": {},
                    "retry_count": 0
                }
                final_state = smith_agent_app.invoke(initial_state)
                
                # Format sub-agent outputs
                response_text = (
                    f"### 🔍 Analysis\n{final_state.get('analysis_summary')}\n\n"
                    f"### 📋 Execution Plan\n" + "\n".join([f"- {s}" for s in final_state.get('plan_steps', [])]) + "\n\n"
                    f"### 🛡️ Audit Status\n**{'✅ Approved' if final_state.get('audit_passed') else '⚠️ Flagged for review'}**"
                )
            else:
                # Fallback: direct model response
                response = llm.invoke(user_query)
                response_text = response.content

            # Render response to screen
            st.markdown(response_text)
            
            # Save assistant response to session memory
            st.session_state.messages.append({"role": "assistant", "content": response_text})
