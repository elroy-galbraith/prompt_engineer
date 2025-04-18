# pages/2_Build_Your_Prompt.py
import streamlit as st
from utils.navigation import go_to_page

st.title("🛠️ Build Your Ideal Prompt")

qa_state = st.session_state.get("qa_state")
if not qa_state or "current_question" not in qa_state:
    st.warning("Please go through the guided Q&A first.")
    st.stop()

strategy = qa_state["current_question"]

st.markdown("### Let's design your prompt:")

with st.form("prompt_builder_form"):
    task = st.text_area("📝 Describe the task you'd like the model to perform")

    examples = []
    if strategy in ["STRATEGY_ONE_SHOT", "STRATEGY_FEW_SHOT"]:
        st.markdown("#### 📌 Provide example(s)")
        examples.append(st.text_area("Example 1"))
        if strategy == "STRATEGY_FEW_SHOT":
            examples.append(st.text_area("Example 2"))
            examples.append(st.text_area("Example 3 (optional)", value="", help="You can leave this blank if not needed."))

    if strategy == "STRATEGY_SYSTEM":
        system_msg = st.text_input("🧠 System Prompt (sets tone, role, or task definition)", value="You are a helpful assistant.")
    else:
        system_msg = ""

    output_format = st.text_input("📤 Desired output format (optional)", placeholder="e.g., JSON, bullet points...")

    submitted = st.form_submit_button("💾 Generate Prompt")

if submitted:
    final_prompt = ""

    if system_msg:
        final_prompt += f"[System Message]\n{system_msg}\n\n"

    if task:
        final_prompt += f"[Task Description]\n{task}\n\n"

    if examples and any(examples):
        final_prompt += "[Examples]\n"
        for i, ex in enumerate(examples):
            if ex.strip():
                final_prompt += f"Example {i+1}:\n{ex.strip()}\n\n"

    if output_format:
        final_prompt += f"[Desired Output Format]\n{output_format}\n"

    # Save it to session state for the next module
    st.session_state["compiled_prompt"] = final_prompt

    st.success("Prompt generated!")
    st.code(final_prompt, language="markdown")
    st.markdown("✅ Ready to test and refine your prompt in the next step!")

# Show navigation button if we have a compiled prompt
if "compiled_prompt" in st.session_state:
    if st.button("Proceed to Evaluation & Refinement"):
        go_to_page("Evaluate and Refine")