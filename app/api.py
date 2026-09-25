from fastapi import FastAPI
from app.config import settings
from app.models import JobRequirement, CandidateResume, ScreeningReport
from app.services.screener import screen_candidate

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.post("/screen", response_model=ScreeningReport)
def screen(payload: dict):
    job = JobRequirement(**payload["job"])
    resume = CandidateResume(**payload["resume"])
    score, matched, missing, rec = screen_candidate(job, resume)
    return ScreeningReport(
        candidate_name=resume.candidate_name,
        role_title=job.role_title,
        match_score=score,
        matched_skills=matched,
        missing_skills=missing,
        recommendation=rec
    )
