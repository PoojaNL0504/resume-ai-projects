# ats_service.py - Functions for calculating ATS score, cleaning text, and saving results to the database

import re
import json
from groq import Groq
from app.db.database import SessionLocal
from app.db.models import ATSResult
from dotenv import load_dotenv
import os       
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

#  CLEAN TEXT 
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text.split()


#  ATS CALCULATION
def calculate_ats_score(resume_text, jd_text):

    prompt = f"""
You are a strict ATS system.

IMPORTANT RULES:
- Return ONLY valid JSON
- Do NOT add explanation
- Do NOT wrap in markdown
- Arrays must contain ONLY plain strings (NO objects)
- ATS score must be between 0 and 100

Format:
{{
  "ats_score": number,
  "summary": "short human-friendly explanation",
  "missing_skills": ["skill1", "skill2"],
  "improvements": ["point1", "point2"]
}}

Resume:
{resume_text}

Job Description:
{jd_text}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    result = response.choices[0].message.content

    print(" RAW LLM RESPONSE:\n", result)

    #  CLEAN RESPONSE 
    cleaned = re.sub(r"```json|```", "", result).strip()

    match = re.search(r"\{[\s\S]*\}", cleaned)
    if match:
        cleaned = match.group()
    else:
        print(" No JSON found")

    try:
        data = json.loads(cleaned)

        data["missing_skills"] = [str(x) for x in data.get("missing_skills", [])]
        data["improvements"] = [str(x) for x in data.get("improvements", [])]
        score = data.get("ats_score", 0)
        if score <= 1:  
            score = score * 100

        data["ats_score"] = round(score, 2)

        return data

    except Exception as e:
        print(" JSON ERROR:", e)
        print("RAW:", result)

        return {
            "ats_score": 0,
            "summary": "Error parsing AI response",
            "missing_skills": [],
            "improvements": ["Retry the request"]
        }


#  SAVE ATS RESULT to DB
def save_ats_result(data, jd,resume_id):

    db = SessionLocal()

    try:
        new_result = ATSResult(
            score=data.get("ats_score", 0),
            missing_skills=",".join(map(str, data.get("missing_skills", []))),
            improvements=",".join(map(str, data.get("improvements", []))),
            resume_id=resume_id   ,
            jd=jd,  

        )

        db.add(new_result)
        db.commit()

    except Exception as e:
        print(" DB ERROR:", e)

    finally:
        db.close()