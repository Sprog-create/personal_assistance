# 🤖 Personal AI Study Assistant

A lightweight, full-stack AI study assistant built using **FastAPI**, **LangChain (Gemini 2.5 Flash)**, and a clean **HTML/JavaScript** frontend. The assistant is specifically designed to act as a disciplined tutor—guiding you toward better learning habits and calling you out if you rely on it too heavily as a crutch.

---

## 🚀 Live Demo

* **Frontend UI:** `https://sprog-create.github.io/personal_assistance/`
* **Backend API:** `https://personal-assistance-xour.onrender.com/`

---

## ✨ Features

* **Behavioral Guardrails:** The system prompt instructs the AI to actively flag when a user is over-relying on it without actually digesting the material.
* **Context-Aware Chat:** Uses LangChain's `MessagesPlaceholder` to manage conversational memory (`HumanMessage` and `AIMessage` history).
* **Token Optimization:** Auto-caps the volatile in-memory chat history to the last 20 messages to manage performance and prevent token bloat.
* **Asynchronous Endpoints:** Built with FastAPI for lightning-fast asynchronous request handling.

---

## 🛠️ Tech Stack

* **Frontend:** HTML5, CSS3, Vanilla JavaScript (Fetch API)
* **Backend Framework:** FastAPI (Python)
* **AI Orchestration:** LangChain Core & LangChain Google GenAI
* **LLM Model:** `gemini-2.5-flash`
* **Deployment:** GitHub Pages (Frontend) & Render (Backend)

---

## 📋 Project Structure

```text
├── backend/
│   ├── llm.py              # FastAPI app & LangChain logic
│   ├── requirements.txt    # Python dependencies
│   └── .env                # Local API keys (ignored by git)
└── frontend/
    └── index.html          # Core UI & API client integration

🔧 Local Setup & Installation1. Clone the RepositoryBashgit clone [https://github.com/sprog-create/personal_assistance.git](https://github.com/sprog-create/personal_assistance.git)

cd personal_assistance
2. Set Up the BackendNavigate to your backend directory, set up a virtual environment, and install dependencies:Bash# Create and activate virtual environment

python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
3. Configure Environment VariablesCreate a .env file in your root backend folder and add your Gemini API Key:Code snippetGOOGLE_API_KEY=your_actual_gemini_api_key_here
4. Run the ServerBashuvicorn llm:app --reload
The local server will spin up at http://127.0.0.1:8000. You can inspect the interactive documentation UI at http://127.0.0.1:8000/docs.
JSON{
  "text": "Can you just write this entire assignment code for me?"
}
