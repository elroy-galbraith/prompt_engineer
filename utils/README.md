# Utils Module Documentation

This directory contains utility modules that support the core functionality of the Prompt Architect application. Each module serves a specific purpose in managing application flow, navigation, and logging.

## Modules Overview

### `navigation.py`
- **Purpose**: Handles page navigation within the Streamlit application
- **Key Functions**:
  - `go_to_page(page_name: str)`: Redirects users between different pages of the application
  - Manages page name mapping and navigation state
  - Integrates with Streamlit's navigation system

### `flow_logic.py`
- **Purpose**: Manages the question flow and answer storage logic
- **Key Functions**:
  - `get_next_question(current_id, answers, return_next_id=False)`: Determines the next question in the flow based on current answers
  - `store_answer(state, qid, answer)`: Stores user answers in the application state
  - Loads and manages question data from `data/questions.json`

### `logger.py`
- **Purpose**: Provides centralized logging functionality for the application
- **Features**:
  - Configures logging with both file and console output
  - Creates daily log files in the `logs` directory
  - Uses a consistent logging format with timestamps
  - Logs are stored in `logs/app_YYYYMMDD.log`

## Usage

To use these utilities in your code:

```python
from utils import logger, navigation, flow_logic

# For logging
logger.info("Your log message")

# For navigation
navigation.go_to_page("Build Your Prompt")

# For flow management
next_question, options = flow_logic.get_next_question(current_id, answers)
```

## Dependencies
- Streamlit (for navigation)
- Python's built-in logging module
- JSON handling for question data

## File Structure
```
utils/
├── __init__.py
├── navigation.py
├── flow_logic.py
└── logger.py
``` 