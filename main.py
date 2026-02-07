from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import uuid

app = FastAPI(title="Envonvia API", version="1.0")

# Memória simples em RAM (MVP)
memory = []

class Interaction(BaseModel):
    user_id: str
    message: str
    feedback: int | None = None

@app.get("/")
def root():
    return {
        "status": "online",
        "name": "Envonvia",
        "time": datetime.utcnow()
    }

@app.post("/interact")
def interact(data: Interaction):
    record = {
        "id": str(uuid.uuid4()),
        "user": data.user_id,
        "message": data.message,
        "feedback": data.feedback,
        "timestamp": datetime.utcnow()
    }
    memory.append(record)

    return {
        "response": "Aprendi com essa interação.",
        "memory_size": len(memory),
        "last_record": record
    }

@app.get("/memory")
def get_memory():
    return memory
