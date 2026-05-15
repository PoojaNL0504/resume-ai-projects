# models.py

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

#  Resume model
class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)

    # relationship
    ats_results = relationship("ATSResult", back_populates="resume")

# ATS Result model
class ATSResult(Base):
    __tablename__ = "ats_results"

    id = Column(Integer, primary_key=True, index=True)

    score = Column(Integer)
    jd = Column(Text)

    missing_skills = Column(Text)
    improvements = Column(Text)

    #  FOREIGN KEY 
    resume_id = Column(Integer, ForeignKey("resumes.id"))

    resume = relationship("Resume", back_populates="ats_results")