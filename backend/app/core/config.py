from pathlib import Path

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents = True,exist_ok=True)

VECTORSTORE_DIR = Path("data/vectorstore")
VECTORSTORE_DIR.mkdir(parents=True,exist_ok=True)

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

TOP_K = 5

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

