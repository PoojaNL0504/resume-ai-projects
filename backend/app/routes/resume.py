# resume.py - Resume upload, parsing, and AI interactions

from fastapi import APIRouter, UploadFile, File
from app.services.parser import extract_text_from_pdf
from app.services.ai_service import extract_skills, rewrite_resume_line, chat_with_resume
from app.services.matcher import match_jobs
from app.models.schema import RewriteRequest, ChatRequest
from app.db.database import SessionLocal
from app.db.models import Resume

# APIRouter instance
router = APIRouter()

resume_text_store = ""

# Upload resume and extract text
@router.post("/upload_resume")
async def upload_resume(file: UploadFile = File(...)):

    global resume_text_store, resume_id_store

    db = SessionLocal()

    text = extract_text_from_pdf(file)

    # save in DB
    new_resume = Resume(content=text)
    db.add(new_resume)
    db.commit()
    db.refresh(new_resume)

    #  store globally
    resume_text_store = text
    resume_id_store = new_resume.id

    db.close()

    return {"message": "Resume uploaded"}

#  REWRITE RESUME LINE
@router.post("/rewrite")
async def rewrite_line(data: RewriteRequest):

    improved = rewrite_resume_line(data.line)
    return {
        "original": data.line,
        "improved": improved
    }


#  CHAT WITH RESUME
@router.post("/chat")
async def chat(data: ChatRequest):

    answer = chat_with_resume(resume_text_store, data.question)
    return {
        "question": data.question,
        "answer": answer
    }