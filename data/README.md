# Data Directory Documentation

This directory contains JSON configuration files that define the application's question flow and prompting strategies. These files are used by the `flow_logic.py` module to guide users through the prompt engineering process.

## Files Overview

### `questions.json`
- **Purpose**: Defines the question flow and branching logic for the prompt engineering process
- **Structure**:
  ```json
  {
    "Q1": {
      "text": "Question text",
      "options": ["Option1", "Option2"],
      "next": {
        "Option1": "NextQuestionID",
        "Option2": "NextQuestionID"
      }
    }
  }
  ```
- **Flow**:
  1. Q1: Determines if examples are needed
  2. Q2: Assesses if one example is sufficient
  3. Q3: Evaluates need for multiple examples
  4. Q4: Checks if system message is required

### `strategies.json`
- **Purpose**: Defines the available prompting strategies and their descriptions
- **Structure**:
  ```json
  {
    "STRATEGY_ID": {
      "title": "Strategy Name",
      "emoji": "Visual Icon",
      "description": "Strategy description"
    }
  }
  ```
- **Available Strategies**:
  - Zero-Shot Prompting (🧊): No examples needed
  - One-Shot Prompting (🎯): Single example required
  - Few-Shot Prompting (📚): Multiple examples needed
  - System Prompting (🧠): System message required

## Usage

These files are automatically loaded by the `flow_logic.py` module in the utils directory. The question flow is used to determine the appropriate prompting strategy based on user responses.

## Data Flow

1. User answers questions from `questions.json`
2. Based on answers, the system determines the next question
3. Eventually leads to a strategy from `strategies.json`
4. The selected strategy guides the prompt engineering process

## File Structure
```
data/
├── questions.json    # Question flow and branching logic
└── strategies.json   # Prompting strategy definitions
``` 