import streamlit as st
import requests

# Configuration
OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama2:latest"  

# Page Setup
st.set_page_config(page_title="Local LLM ChatBot", page_icon="💬", layout="wide")

# Session State Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar - Conversation History
with st.sidebar:
    st.header("💬 Conversation History")
    if st.session_state.messages:
        for sender, text in st.session_state.messages:
            st.markdown(f"**{sender}:** {text}")
    else:
        st.write("No conversation yet.")
    
    if st.button("🔄 Reset Conversation"):
        st.session_state.messages = []
        st.experimental_rerun()

# Main Chat Interface
st.title("💬 Local LLM Personal Chatbot")
st.write("Chat with your locally running Ollama model (llama2).")

# User input form
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Your Message", placeholder="Type your question here...")
    submitted = st.form_submit_button("Send")

if submitted and user_input.strip():
    # Append user message
    st.session_state.messages.append(("You", user_input))

    # Send to Ollama API with streaming disabled

    try:
        payload = {
            "model": MODEL_NAME,
            "prompt": user_input,
            "stream": False 
        }
        response = requests.post(OLLAMA_API_URL, json=payload)

        if response.status_code == 200:
            model_reply = response.json().get("response", "").strip()
            st.session_state.messages.append(("LLM", model_reply))
        else:
            st.session_state.messages.append(("LLM", f"Error {response.status_code}: {response.text}"))
    except Exception as e:
        st.session_state.messages.append(("LLM", f"Connection error: {e}"))


# Display Chat Messages
for sender, text in st.session_state.messages:
    if sender == "You":
        st.markdown(f"**🧑 {sender}:** {text}")
    else:
        st.markdown(f"**🤖 {sender}:** {text}")
