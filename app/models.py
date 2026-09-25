from pydantic import BaseModel
from typing import List, Dict

class JobRequirement(BaseModel):
    role_title: str
    required_skills: List[str]
    min_years_experience: int

class CandidateResume(BaseModel):
    candidate_name: str
    extracted_skills: List[str]
    years_experience: int
    raw_resume_text: str

class ScreeningReport(BaseModel):
    candidate_name: str
    role_title: str
    match_score: int
    matched_skills: List[str]
    missing_skills: List[str]
    recommendation: str
