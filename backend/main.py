from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.documents import router as documents_router

app = FastAPI(title="RAG Document Chat")
app.include_router(documents_router,prefix = "/api/documents")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]

)

@app.get("/health")
def health():
    return {"status":"ok"}


