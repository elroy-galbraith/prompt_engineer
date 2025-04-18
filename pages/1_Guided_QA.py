# pages/1_Guided_QA.py
import streamlit as st
import json
from pathlib import Path
from utils.flow_logic import get_next_question, store_answer
from utils.navigation import go_to_page

# Load strategies
STRATEGIES_PATH = Path("data/strategies.json")
strategies = json.loads(STRATEGIES_PATH.read_text())

st.title("🧭 Guided Prompt Design")

# Add Start Over button at the top
if st.button("🔄 Start Over"):
    st.session_state.qa_state = {
        "answers": {},
        "current_question": "Q1"
    }
    st.rerun()

if "qa_state" not in st.session_state:
    st.session_state.qa_state = {
        "answers": {},
        "current_question": "Q1"
    }

qa_state = st.session_state.qa_state
answers = qa_state["answers"]
question_id = qa_state["current_question"]

# Check if we've reached a strategy or end
if question_id.startswith("STRATEGY_") or question_id == "END":
    st.success("All done! Here's your recommended strategy:")
    strategy = strategies.get(question_id, {})
    st.markdown(f"{strategy.get('emoji', '🔧')} **{strategy.get('title', 'Unknown Strategy')}**: {strategy.get('description', '')}")
    st.markdown("---")
    st.markdown("### Ready to build your prompt?")
    if st.button("Proceed to Prompt Builder"):
        go_to_page("Build Your Prompt")
    st.stop()

question, options = get_next_question(question_id, answers)

st.markdown(f"### {question}")
selected = st.radio("Choose one:", options)

if st.button("Next"):
    store_answer(qa_state, question_id, selected)
    next_q = get_next_question(question_id, answers, return_next_id=True)
    qa_state["current_question"] = next_q
    st.rerun()