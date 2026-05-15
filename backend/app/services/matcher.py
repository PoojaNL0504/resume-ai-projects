# matcher.py - Simple job matching logic based on user skills and job requirements

import json
import os

# Sample job data for matching
def get_sample_jobs():
    file_path = os.path.join(os.path.dirname(__file__), "jobs.json")

    with open(file_path, "r") as f:
        return json.load(f)

# Match user skills with job requirements
def match_jobs(user_skills):
    jobs = get_sample_jobs()

    matched_jobs = []

    user_skills = [skill.strip().lower() for skill in user_skills.split(",")]

    for job in jobs:
        job_skills = job["skills"]

        matched = set(user_skills) & set(job_skills)
        score = int((len(matched) / len(job_skills)) * 100)

        matched_jobs.append({
            "job_title": job["title"],
            "match_score": score,
            "matched_skills": list(matched),
            "missing_skills": list(set(job_skills) - set(user_skills))
        })

    return matched_jobs