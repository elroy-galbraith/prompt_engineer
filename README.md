# MyPrompts

## 🌟 User Journey Breakdown

1. 🧭 Guided Q&A Flow (based on the diagram)
Users are walked through a set of binary or multiple-choice questions — like a decision tree. Each answer navigates the diagram’s logic (e.g., “Do you need specific examples?”, “Is the task code-related?”).

2.	🧠 Recommendation Engine
Based on the answers, the app suggests the ideal prompting strategy (e.g., Zero-shot, Chain-of-Thought, Role Prompting, etc.), and possibly more than one if the scenario is complex.

3.	✍️ Prompt Builder UI
Once a strategy is selected, the app shows relevant input fields — such as:
- Task instructions
- Examples (1-shot / few-shot)
- System prompt (if applicable)
- Role description
- Contextual background
- Code snippets (if code-related)
- Desired output format
- Temperature, token limit, etc.

5.	🧩 Prompt Compiler
The app dynamically builds the full prompt using best practices and sections the user has filled in. It shows a preview of the final prompt that can be copied or exported.

6.	🧪 Prompt Evaluation Module
Users can input the prompt into an OpenAI/GPT call, test the result, and rate the output using sliders, radio buttons, or text feedback.
Optionally, the system can offer:
- Auto-suggestions on how to improve it
- A “history” of attempts
- A button to restart or tweak parameters

⸻

## 🛠️ Tools & Tech Stack

- Streamlit — Core UI
- Session State — For storing progress along the decision tree
- Mermaid.js (via st_mermaid) — To optionally show the original flow diagram inline
- Prompt Template Builder — Custom Python logic for assembling prompts
- LLM Integration (optional) — To evaluate the prompts and assist with revisions (e.g., OpenAI API)

⸻

## ✅ Code structured into:
- main.py
- prompt_builder.py
- prompt_templates.py
- evaluation.py
  
