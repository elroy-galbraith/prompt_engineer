import streamlit as st
from .logger import logger

def go_to_page(page_name: str):
    """Redirect user to another page using Streamlit's navigation."""
    # Convert to the correct page name format (e.g., "Build Your Prompt" -> "2_Build_Your_Prompt")
    page_mapping = {
        "Build Your Prompt": "2_Build_Your_Prompt",
        "Evaluate and Refine": "3_Evaluate_and_Refine"
    }
    page_id = page_mapping.get(page_name, page_name)
    
    logger.info(f"Navigating from {st.session_state.get('current_page', 'Home')} to {page_name}")
    # Use Streamlit's navigation
    st.switch_page(f"pages/{page_id}.py") 