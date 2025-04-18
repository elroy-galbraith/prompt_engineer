# pages/3_Evaluate_and_Refine.py
import streamlit as st
import requests
import json
from datetime import datetime

st.title("🧪 Evaluate & Refine Your Prompt")

compiled_prompt = st.session_state.get("compiled_prompt", "")

if not compiled_prompt:
    st.warning("No prompt found. Please go back and build one first.")
    st.stop()

st.markdown("### ✨ Your Current Prompt")
st.code(compiled_prompt, language="markdown")

st.markdown("### 🧠 Optional: Run the Prompt via OpenRouter")

# Get API key from secrets
api_key = st.secrets["openrouter"]["API_KEY"]
if not api_key:
    st.error("OpenRouter API key not found in secrets.toml. Please add it to continue.")
    st.stop()

# Add test input section
st.markdown("### 📝 Test Input")
test_input = st.text_area("Provide an example input to test your prompt with:", 
                         placeholder="Enter your test case here...",
                         help="This will be combined with your prompt to test the model's response.")

with st.expander("⚙️ Configure Model Settings"):
    site_url = st.text_input("Site URL (optional)", placeholder="https://your-site.com")
    site_name = st.text_input("Site Name (optional)", placeholder="Your Site Name")
    model_choice = st.selectbox("Choose a model", [
        "openai/o4-mini-high",
        "anthropic/claude-3-haiku:beta",
        "google/gemini-2.5-pro-preview-03-25",
        "deepseek/deepseek-v3-base:free",
        "shisa-ai/shisa-v2-llama3.3-70b:free"
    ])
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)
    max_tokens = st.number_input("Max Tokens", 100, 2000, 500, 100)
    run_prompt = st.button("▶️ Run Prompt")

if run_prompt:
    if not test_input.strip():
        st.warning("Please provide a test input before running the prompt.")
        st.stop()
        
    with st.spinner("Getting response..."):
        try:
            headers = {
                "Authorization": f"Bearer {api_key}",
            }
            
            # Add optional headers if provided
            if site_url:
                headers["HTTP-Referer"] = site_url
            if site_name:
                headers["X-Title"] = site_name
            
            # Combine the prompt with the test input
            full_prompt = f"{compiled_prompt}\n\nInput: {test_input}"
            
            # Store model settings
            model_settings = {
                "model": model_choice,
                "temperature": temperature,
                "max_tokens": max_tokens,
                "site_url": site_url,
                "site_name": site_name
            }
            
            response = requests.post(
                url="https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json={
                    "model": model_choice,
                    "messages": [
                        {
                            "role": "user",
                            "content": full_prompt
                        }
                    ],
                    "temperature": temperature,
                    "max_tokens": max_tokens
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                reply = result['choices'][0]['message']['content']
                st.markdown("### 💬 Response from OpenRouter")
                st.code(reply, language="markdown")
                
                # Store the response and settings in session state
                st.session_state["last_response"] = reply
                st.session_state["last_settings"] = model_settings
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
                
        except Exception as e:
            st.error(f"Something went wrong: {str(e)}")

st.markdown("### ✅ Evaluate the Output")
evaluation = st.radio("Was the output helpful?", ["👍 Yes", "👎 No", "🟡 Somewhat"])
feedback = st.text_area("📝 What would you change or try next?", placeholder="E.g., Add more examples, be more specific...")

if st.button("💾 Save Evaluation"):
    # Initialize evaluations in session state if not exists
    if "evaluations" not in st.session_state:
        st.session_state.evaluations = []
    
    # Add new evaluation
    st.session_state.evaluations.append({
        "timestamp": datetime.now().isoformat(),
        "prompt": compiled_prompt,
        "test_input": test_input,
        "response": st.session_state.get("last_response", ""),
        "settings": st.session_state.get("last_settings", {}),
        "rating": evaluation,
        "feedback": feedback
    })
    
    st.success("Feedback saved! You can now go back to the prompt builder to iterate.")
    
    # Show evaluation history
    st.markdown("### 📊 Evaluation History")
    for eval in reversed(st.session_state.evaluations):
        with st.expander(f"Evaluation from {datetime.fromisoformat(eval['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}"):
            st.markdown(f"**Rating:** {eval['rating']}")
            st.markdown(f"**Feedback:** {eval['feedback']}")
            
            # Display model settings
            st.markdown("**Model Settings:**")
            settings = eval.get("settings", {})
            st.markdown(f"- Model: {settings.get('model', 'N/A')}")
            st.markdown(f"- Temperature: {settings.get('temperature', 'N/A')}")
            st.markdown(f"- Max Tokens: {settings.get('max_tokens', 'N/A')}")
            if settings.get('site_url'):
                st.markdown(f"- Site URL: {settings['site_url']}")
            if settings.get('site_name'):
                st.markdown(f"- Site Name: {settings['site_name']}")
            
            st.markdown("**Test Input:**")
            st.code(eval['test_input'])
            st.markdown("**Response:**")
            st.code(eval['response'])