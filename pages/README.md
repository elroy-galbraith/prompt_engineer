# Pages Directory Documentation

This directory contains the main interactive pages of the Prompt Engineering Assistant application. Each page represents a step in the prompt engineering workflow.

## Overview

The application follows a sequential workflow with three main pages:

1. **Guided Q&A** (`1_Guided_QA.py`)
2. **Prompt Builder** (`2_Build_Your_Prompt.py`)
3. **Evaluate & Refine** (`3_Evaluate_and_Refine.py`)

## Page Descriptions

### 1. Guided Q&A (`1_Guided_QA.py`)
- **Purpose**: Helps users determine the most appropriate prompt engineering strategy through an interactive questionnaire
- **Key Features**:
  - Interactive question flow based on user responses
  - Strategy recommendations based on answers
  - Session state management for tracking progress
  - "Start Over" functionality
- **Dependencies**:
  - `utils/flow_logic.py` for question flow management
  - `utils/navigation.py` for page navigation
  - `data/strategies.json` for strategy definitions

### 2. Build Your Prompt (`2_Build_Your_Prompt.py`)
- **Purpose**: Provides an interface for users to construct their prompt based on the recommended strategy
- **Key Features**:
  - Dynamic form based on selected strategy
  - Support for different prompt types (one-shot, few-shot, system prompts)
  - Optional output format specification
  - Automatic prompt compilation
- **Dependencies**:
  - `utils/navigation.py` for page navigation
  - Session state from Guided Q&A

### 3. Evaluate & Refine (`3_Evaluate_and_Refine.py`)
- **Purpose**: Allows users to test, evaluate, and refine their prompts
- **Key Features**:
  - OpenRouter API integration for prompt testing
  - Configurable model settings
  - Response evaluation and feedback collection
  - Evaluation history tracking
- **Dependencies**:
  - OpenRouter API key (via secrets.toml)
  - Session state from previous pages

## Session State Management

The application uses Streamlit's session state to maintain data between pages. Key session state variables include:

- `qa_state`: Stores the current question and answers from the Guided Q&A
- `compiled_prompt`: Stores the final prompt from the Prompt Builder
- `evaluations`: Stores the history of prompt evaluations

## Getting Started

1. Ensure all dependencies are installed
2. Configure the OpenRouter API key in `secrets.toml`
3. Run the application using Streamlit
4. Follow the sequential workflow through the pages

## Contributing

When adding new features or modifying existing ones:

1. Maintain the sequential numbering of pages
2. Update this README with any new functionality
3. Ensure proper session state management
4. Add appropriate error handling and user feedback
5. Test the workflow end-to-end

## Notes

- The application is designed to be used sequentially
- Each page validates the presence of required session state
- Error handling and user guidance are implemented throughout
- The evaluation history persists during the session 