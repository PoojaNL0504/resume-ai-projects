# main.py - FastAPI application setup and route inclusion

from fastapi import FastAPI
from app.routes import resume
from app.routes import ats
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

# include resume router
app.include_router(resume.router)

@app.get("/")
def home():
    return {"message":"FastAPI is running"}

# CORS middleware (allow all for now, can be restricted in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for now)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# include ATS router
app.include_router(ats.router)