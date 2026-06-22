from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# In-memory chat history (per server instance)
# Each entry is a HumanMessage or AIMessage object
chat_history: list = []

template = ChatPromptTemplate.from_messages([
    ("system", (
        "You are a helpful study assistant. "
        "You point out when someone is using you more than required and is not actually learning anything. "
        "You also give them tips on how to learn better and not just use you as a crutch."
    )),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])


class Message(BaseModel):
    text: str


@app.get("/")
async def home():
    return {"status": "AI Assistant API is running. POST to /chat to interact."}


@app.post("/chat")
async def chat(msg: Message):
    global chat_history

    # Build prompt with proper LangChain message objects
    prompt = template.invoke({"input": msg.text, "history": chat_history})
    result = llm.invoke(prompt)

    # Append to in-memory history as proper message objects
    chat_history.append(HumanMessage(content=msg.text))
    chat_history.append(AIMessage(content=result.content))

    # Optional: cap history to last 20 messages to avoid token bloat
    if len(chat_history) > 20:
        chat_history = chat_history[-20:]

    return {"reply": result.content}


@app.delete("/chat/history")
async def clear_history():
    """Clear the in-memory chat history."""
    global chat_history
    chat_history = []
    return {"status": "History cleared."} 