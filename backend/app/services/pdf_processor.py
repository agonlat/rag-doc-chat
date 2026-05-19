import fitz
import re
from pathlib import Path
from app.core.config import CHUNK_SIZE, CHUNK_OVERLAP

def extract_text_per_page(pdf_path:Path) -> list[tuple[int,str]]:
    pages = []
    doc = fitz.open(str(pdf_path))

    for page_num in range(len(doc)):
        text = doc[page_num].get_text("text")
        text = text.strip()
        if text:
            pages.append((page_num + 1, text))
            
    doc.close()
    return pages

def chunk_text(text: str) ->list[str]:
    sentences = re.split(r"(?<=[.!?])\s+",text)
    sentences = [s.strip() for s in sentences if len(s.strip()>20)]

    chunks = []
    current_chunk = []
    current_len = 0

    for sentence in sentences:
        if current_len + len(sentence) > CHUNK_SIZE and current_chunk:
            chunks.append(" ".join(current_chunk))

            overlap = []
            overlap_len = 0
            for s in reversed(current_chunk):
                if overlap_len + len(s) <= CHUNK_OVERLAP:
                    overlap.insert(0, s)
                    overlap_len += len(s)
                else:
                    break

                current_chunk = overlap
                current_len = overlap_len
            
            current_chunk.append(sentence)
            current_len = overlap_len

        current_chunk.append(sentence)
        current_len += len(sentence)

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks



def process_pdf(pdf_path:Path, doc_id:str, doc_name:str)->list[dict]:
    pages = extract_text_per_page(pdf_path)
    all_chunks = []

    for page_num,page_text in pages:
        chunks = chunk_text(page_text)

        for chunk in chunks:
            all_chunks.append({
                "text":chunk,
                "doc_id":doc_id,
                "doc_name":doc_name,
                "page":page_num
            })

    return all_chunks

