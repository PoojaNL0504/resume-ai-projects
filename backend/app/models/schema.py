# schema.py

from pydantic import BaseModel

# Pydantic models for request/response validation

class RewriteRequest(BaseModel):
    line: str

class ChatRequest(BaseModel):
    question: str