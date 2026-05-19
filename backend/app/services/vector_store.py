import faiss
import numpy as np
import pickle
from patlib import Path
from sentence_transformers import SentenceTransformer
from app.core.config import EMBEDDING_MODEL, VECTORSTORE_DIR, TOP_K

model = SentenceTransformer(EMBEDDING_MODEL)
DIMENSION = 384

def get_paths() -> tuple[Path, Path]:
    index_path = VECTORSTORE_DIR / "faiss.index"
    meta_path = VECTORSTORE_DIR / "metadata.pkl"
    return index_path, meta_path

def load_store() -> tuple[faiss.Idex, list[dict]]:
    index_path, meta_path = get_paths()

    if index_path.exists() and meta_path.exists():
        index = faiss.read_index(str(index_path))
        with open(meta_path, "rb") as f:
            chunks = pickle.load(f)
            return index, chunks
        
    index = faiss.IndexFlatIP(DIMENSION)
    return index, []

