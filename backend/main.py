from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="RAG Document Chat")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_origins=["*"],
    allow_origins=["*"]

)

@app.get("/health")
def health():
    return {"status":"ok"}

