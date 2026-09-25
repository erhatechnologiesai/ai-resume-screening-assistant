import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestResumeScreening(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_screening_logic(self):
        payload = {
            "job": {
                "role_title": "AI Automation Engineer",
                "required_skills": ["Python", "FastAPI", "LangChain", "Docker"],
                "min_years_experience": 3
            },
            "resume": {
                "candidate_name": "Hamza Tariq",
                "extracted_skills": ["Python", "FastAPI", "Docker", "PostgreSQL"],
                "years_experience": 4,
                "raw_resume_text": "Experienced Python and FastAPI backend engineer with 4 years deploying containerized apps."
            }
        }
        res = self.client.post("/screen", json=payload)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertGreaterEqual(data["match_score"], 75)
        self.assertEqual(data["recommendation"], "ADVANCE_TO_TECHNICAL_INTERVIEW")

if __name__ == "__main__":
    unittest.main()
