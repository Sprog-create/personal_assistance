from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder 
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

from fastapi import FastAPI
from fastapi.responses import FileResponse





load_dotenv()

# Initialize the LLM (don't invoke it here, just set it up)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3,)



# Start the server
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_methods=["*"], allow_headers=["*"])

class Message(BaseModel):
    text: str

@app.get("/")
async def home():
    return FileResponse("index.html")

@app.post("/chat")
async def chat(msg: Message):
      template = ChatPromptTemplate.from_messages([
    ("system", "you are a helpful study assistant, but you point out when someone is using you more than required and is not actually learning anything, you also give them tips on how to learn better and not just use you as a crutch"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])
      chat_history=[]
#load chat history
      with open('chat_history.txt') as f:
       chat_history.extend(f.readlines())
      prompt = template.invoke({"input": msg.text, "history": chat_history})  # history is empty for now
      result = llm.invoke(prompt)
        # .content extracts just the text

      with open("chat_history.txt", "a") as f:
        f.write(f"Human:{msg.text}\n")
        f.write(f"AI:{result.content}\n")
        return {"reply": result.content}