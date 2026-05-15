
# ats.py - ATS score calculation and endpoint

from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ats_service import calculate_ats_score, save_ats_result
from app.db.database import SessionLocal
from app.db.models import Resume

# APIRouter instance
router = APIRouter()

# Pydantic model for incoming request
class ATSRequest(BaseModel):
    jd: str

resume_text_store = ""
resume_id_store = None  # 

# Calculate ATS score
@router.post("/check_ats")
def check_ats(data: ATSRequest):

    db = SessionLocal()

    #  always fetch latest resume
    resume = db.query(Resume).order_by(Resume.id.desc()).first()
    if not resume:
        return {
            "ats_score": 0,
            "summary": "Please upload resume first",
            "missing_skills": [],
            "improvements": []
        }

    result = calculate_ats_score(resume.content, data.jd)
    save_ats_result(result, data.jd, resume.id)
    db.close()

    return result