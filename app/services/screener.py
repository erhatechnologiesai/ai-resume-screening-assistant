from app.models import JobRequirement, CandidateResume

def screen_candidate(job: JobRequirement, resume: CandidateResume):
    job_skills = {s.lower() for s in job.required_skills}
    cand_skills = {s.lower() for s in resume.extracted_skills}
    
    matched = list(job_skills.intersection(cand_skills))
    missing = list(job_skills.difference(cand_skills))
    
    skill_ratio = len(matched) / max(len(job_skills), 1)
    exp_ratio = min(1.0, resume.years_experience / max(job.min_years_experience, 1))
    
    score = int((skill_ratio * 70) + (exp_ratio * 30))
    
    if score >= 75:
        rec = "ADVANCE_TO_TECHNICAL_INTERVIEW"
    elif score >= 50:
        rec = "CONSIDER_FOR_JUNIOR_OR_ALTERNATIVE_ROLE"
    else:
        rec = "DO_NOT_PROCEED"

    return score, matched, missing, rec
