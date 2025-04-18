# utils/flow_logic.py
import json
from pathlib import Path
from .logger import logger

QUESTIONS_PATH = Path("data/questions.json")
questions = json.loads(QUESTIONS_PATH.read_text())

def get_next_question(current_id, answers, return_next_id=False):
    # If we've reached a strategy or END, return it
    if current_id.startswith("STRATEGY_") or current_id == "END":
        logger.info(f"Reached end of flow with {current_id}")
        if return_next_id:
            return current_id
        return None, None
    
    q = questions[current_id]
    next_id = q["next"].get(answers.get(current_id), "END")
    logger.info(f"Moving from question {current_id} to {next_id}")
    
    if return_next_id:
        return next_id
    return q["text"], q["options"]

def store_answer(state, qid, answer):
    logger.info(f"Storing answer for question {qid}: {answer}")
    state["answers"][qid] = answer