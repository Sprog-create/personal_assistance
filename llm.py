from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder 
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage



load_dotenv()

# Initialize the LLM (don't invoke it here, just set it up)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.3,)



# Start the server
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_methods=["*"], allow_headers=["*"])

class Message(BaseModel):
    text: str

@app.post("/chat")
async def chat(msg: Message):
      template = ChatPromptTemplate.from_messages([
    ("system", "you are a mean assistant who only replies sarcastically. But also you always answer the question, no matter how rude you are."),
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