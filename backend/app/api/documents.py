from fastapi import APIRouter, UploadFile, File
import uuid
import shutil
from pathlib import Path
from app.core.config import UPLOAD_DIR
from app.services.pdf_processor import process_pdf
from app.services.vector_store import add_chunks
from typing import List

router = APIRouter()

@router.post("/upload")
async def upload_documents(files:List[UploadFile] = File(...)):
    for file in files:
        doc_id = str(uuid.uuid4())
        save_path = UPLOAD_DIR / f"{doc_id}.pdf"
        with open(save_path, "wb") as f:
            shutil.copyfileobj(file.file,f)
        chunks = process_pdf(save_path, doc_id, file.filename)
        add_chunks(chunks)

    return {"status":"ok"}