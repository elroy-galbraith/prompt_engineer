# app.py
import streamlit as st
from utils.logger import logger

logger.info("Application started")
st.set_page_config(
    page_title="Prompt Architect",
    page_icon="🧠",
    layout="centered"
)

logger.info("Setting up home page")
st.title("🤖 Prompt Architect")
st.markdown("""
Welcome! This tool helps you design the ideal prompt for your AI task through guided questions and interactive feedback.

👉 Click on **"Guided QA"** in the sidebar to begin!
""")