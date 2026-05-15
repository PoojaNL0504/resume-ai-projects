# ai_service.py - AI-related functions for skill extraction, resume rewriting, and chat interactions

from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv() 

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

#  CLEAN TEXT 
def extract_skills(text):
    prompt = f"""
    Extract key skills from the following resume.
    Return skills as a clean comma-separated list.

    Resume:
    {text}
    """
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

# REWRITE RESUME LINE
def rewrite_resume_line(line):
    prompt = f"""
    Rewrite the following resume bullet point.

    Rules:
    - Return ONLY one improved sentence
    - Do NOT give multiple options
    - Do NOT give explanation
    - Keep it concise and professional
    - Make it ATS-friendly

    Input:
    {line}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()


# CHAT WITH RESUME
def chat_with_resume(question, resume_text):
    prompt = f"""
You are a smart AI assistant.

User message:
{question}

Resume (optional):
{resume_text if resume_text else "Not provided"}

Instructions:
- If user asks for programming (Python, coding, etc) → answer directly with useful content
- If user asks for interview questions → GIVE questions (don’t ask back)
- If user greets → respond casually
- Only talk about resume if user explicitly asks
- Be direct, helpful, and not repetitive

Now respond to the user.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content
