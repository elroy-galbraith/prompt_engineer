# 🧠 Prompt Architect

A sophisticated prompt engineering system built with Streamlit that guides users through creating optimal prompts for AI tasks.

## 🎯 Features

1. **🔍 Guided Q&A Flow**
   - Interactive decision tree for prompt strategy selection
   - Binary and multiple-choice questions
   - Dynamic navigation based on user responses

2. **🤖 Smart Recommendation Engine**
   - Suggests optimal prompting strategies based on user needs
   - Supports multiple strategies for complex scenarios
   - Includes Zero-shot, Chain-of-Thought, Role Prompting, and more

3. **🛠️ Interactive Prompt Builder**
   - Dynamic input fields based on selected strategy
   - Support for:
     - 📝 Task instructions
     - 📚 Examples (1-shot / few-shot)
     - ⚙️ System prompts
     - 👤 Role descriptions
     - 🌍 Contextual background
     - 💻 Code snippets
     - 📊 Output format specifications
     - 🌡️ Model parameters (temperature, token limits)

4. **🔨 Prompt Compiler**
   - Dynamic prompt assembly
   - Best practices integration
   - Real-time preview
   - Copy/export functionality

5. **📊 Prompt Evaluation**
   - Test prompts with AI models
   - Rate outputs using interactive controls
   - Track improvement history
   - Receive auto-suggestions for optimization

## 🛠️ Tech Stack

- **🎨 Streamlit** - Modern web interface
- **🐍 Python 3.11+** - Core programming language
- **📦 Poetry** - Dependency management
- **👀 Watchdog** - File system monitoring
- **🌐 Requests** - HTTP client for API interactions

## 📁 Project Structure

```
./
├── 🏠 Home.py                # Main application entry point
├── 📄 pages/                 # Streamlit pages
│   ├── 1️⃣ 1_Guided_QA.py    # Initial question flow
│   ├── 2️⃣ 2_Build_Your_Prompt.py  # Prompt construction interface
│   └── 3️⃣ 3_Evaluate_and_Refine.py  # Prompt testing and refinement
├── 🛠️ utils/                 # Utility modules
│   ├── 🔄 flow_logic.py     # Question flow logic
│   ├── 🧭 navigation.py     # Navigation utilities
│   └── 📝 logger.py         # Logging configuration
├── 📚 data/                  # Data files
│   ├── ❓ questions.json    # Question data
│   └── 🎯 strategies.json   # Prompting strategies
├── ⚙️ .streamlit/           # Streamlit configuration
├── 📦 pyproject.toml        # Poetry configuration
└── 🔒 poetry.lock           # Dependency lock file
```

## 🚀 Getting Started

1. **📥 Install Poetry** (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **📦 Install Dependencies**:
   ```bash
   poetry install
   ```

3. **▶️ Run the Application**:
   ```bash
   poetry run streamlit run Home.py
   ```

## 📜 License

This project is licensed under the terms included in the LICENSE file.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
  
