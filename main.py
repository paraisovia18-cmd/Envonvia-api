from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import uuid

app = FastAPI(title="API Envolvia", version="1.0")

# Memória simples em RAM (por enquanto)
memory = []

class ChatInput(BaseModel):
    user_id: str
    message: str

class ChatResponse(BaseModel):
    reply: str
    memory_size: int
    time: str

@app.get("/")
def root():
    return {
        "status": "online",
        "name": "Envolvia",
        "time": datetime.utcnow().isoformat()
    }

@app.post("/chat", response_model=ChatResponse)
def chat(data: ChatInput):
    interaction_id = str(uuid.uuid4())

    # Resposta simples (placeholder de IA)
    reply = f"Recebi sua mensagem: '{data.message}'"

    # Salva na memória
    memory.append({
        "id": interaction_id,
        "user_id": data.user_id,
        "message": data.message,
        "reply": reply,
        "time": datetime.utcnow().isoformat()
    })

    return {
        "reply": reply,
        "memory_size": len(memory),
        "time": datetime.utcnow().isoformat()
    }

@app.get("/memory")
def get_memory():
    return {
        "total_interactions": len(memory),
        "data": memory
    }
