Local LLM Chat is a lightweight web-based chatbot built with Streamlit that communicates directly with a locally installed Large Language Model (LLM) through Ollama.
With a simple and clean interface, you can chat with models like "llama2:latest" fully offline. The app includes a conversation history panel, a reset button, and uses a modern, responsive layout.

Key Features:
1. Chat in real-time with a local LLM — no cloud required
2. Conversation history stored in session
3. One-click reset for fresh chats
4. Simple to run and customize for your own models

How to Run?
1️⃣ Clone the repository
git clone https://github.com/YOUR_USERNAME/local-llm-chat.git
cd local-llm-chat

2️⃣ Install Python dependencies
pip install -r requirements.txt

3️⃣ Make sure Ollama is installed and runningDownload from: https://ollama.ai/downloadThen pull the model you want to use:
ollama pull llama2:latest

4️⃣ Run the Streamlit app
streamlit run app.py

5️⃣ Open your browserGo to: 
http://localhost:8501 and start chatting!


Note: The source code is mainly AI Generated and this project is my first ever step into local LLMs. (I prefer honesty)
