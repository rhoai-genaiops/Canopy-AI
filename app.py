import os
import requests
import streamlit as st
from PIL import Image

# Load environment variable
LLM_ENDPOINT = os.getenv("LLM_ENDPOINT")

# Page setup
st.set_page_config(
    page_title="Canopy AI - Educational Assistant",
    page_icon="🌿",
    layout="wide",
)

# Sidebar navigation
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/4273/4273783.png", width=100)
st.sidebar.title("Canopy AI 🌿")
feature = st.sidebar.radio(
    "Choose a feature:",
    ["Summarization", "Content Creation (coming soon)", "Assignment Scoring (coming soon)"],
    index=0
)

# Main view depending on feature
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color: #2e8b57;'>Canopy AI</h1>
        <p style='font-size: 1.2em;'>Your leafy smart companion for education ✨</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

if feature == "Summarization":
    st.header("🌱 Summarize My Text")
    user_input = st.text_area("Paste your text here:", height=300)

    if st.button("Summarize 🌿"):
        if not user_input.strip():
            st.warning("Please enter some text to summarize.")
        elif not LLM_ENDPOINT:
            st.error("LLM_ENDPOINT not configured in environment variables.")
        else:
            with st.spinner("Talking to the forest spirits..."):
                try:
                    response = requests.post(LLM_ENDPOINT, json={"text": user_input})
                    response.raise_for_status()
                    summary = response.json().get("summary", "(No summary returned)")
                    st.success("Here's your summary:")
                    st.text_area("Summary", summary, height=200)
                except Exception as e:
                    st.error(f"Something went wrong: {e}")
else:
    st.info("This feature is coming soon. Stay tuned!")
