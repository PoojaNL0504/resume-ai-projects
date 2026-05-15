# AI Resume Analyzer and Job Matching System

## Overview
This project is an AI-powered Resume Analysis and Job Matching System designed to help users improve their resumes, evaluate ATS compatibility, and receive role-based insights.

The application allows users to upload resumes, analyzes content using AI, and provides actionable suggestions to enhance job readiness.

## Objective
- Improve resume quality using AI-driven analysis
- Evaluate ATS compatibility and identify missing skills
- Provide structured feedback for better job alignment
- Demonstrate real-world full-stack AI integration

## Features

### 1. Resume Upload and Parsing
- Upload resumes in PDF/DOCX format
- Extracts and processes text content

### 2. Resume Analysis
- Identifies skills and experience
- Detects missing keywords
- Provides improvement suggestions

### 3. ATS Score Checker
- Calculates ATS compatibility score
- Highlights missing skills
- Suggests improvements for better matching

### 4. AI-Based Insights
- Uses LLM-based processing for analysis
- Generates structured feedback

## Tech Stack

### Frontend
- HTML5  
- CSS3  
- JavaScript (ES6)  

### Backend
- FastAPI (Python)

### AI Processing
- LLM (Groq / OpenAI compatible)
- NLP-based text analysis

### Database
- PostgreSQL

### Deployment
- Render (Backend)
- Vercel (Frontend)

## Project Structure

```
backend/
 ├── app/
 │   ├── routes/
 │   ├── services/
 │   ├── db/
 │   └── main.py
frontend/
 ├── index.html
 ├── styles.css
 └── script.js
```

## Setup Instructions

### 1. Clone the Repository
```
git clone https://github.com/your-username/resume-ai-project.git
cd resume-ai-project
```

### 2. Backend Setup

```
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Environment Variables

Create a `.env` file in backend:

```
DATABASE_URL=your_postgresql_url
GROQ_API_KEY=your_api_key
```

### 4. Run Backend

```
uvicorn app.main:app --reload
```

### 5. Frontend Setup

Open frontend files directly or deploy using Vercel.

Update API base URL in frontend:

```
const BASE_URL = "https://your-render-backend-url"
```

### 6. Deployment

#### Backend (Render)
- Create Web Service
- Add environment variables:
  - DATABASE_URL
  - GROQ_API_KEY
- Deploy

#### Frontend (Vercel)
- Import repository
- Set project root (if needed)
- Deploy

## API Endpoints

- `POST /upload_resume` → Upload resume
- `POST /check_ats` → Get ATS score and analysis
- `GET /` → Health check

## Future Improvements
- User authentication
- Dashboard for tracking resumes
- Resume download (PDF generation)
- Advanced job matching system

## License
This project is for educational and demonstration purposes.