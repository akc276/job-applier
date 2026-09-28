import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "src"))

from job_applier.repository.history_repository import check_cooldown, save_job, normalize_domain

class TestHistoryRepository(unittest.TestCase):

    def test_normalize_domain(self):
        self.assertEqual(normalize_domain("Swiggy India Pvt Ltd"), "swiggyindiapvtltd")

    def test_cooldown_check(self):
        cooldown = check_cooldown("NewTestCompany")
        self.assertFalse(cooldown["is_cooldown"])

    def test_save_job(self):
        job_data = {
            "title": "Angular Developer Test",
            "company": "TestCo",
            "location": "India",
            "job_url": "https://testco.com/job/123",
            "match_score": 85,
            "referral_prob_score": 90,
            "safety_score": 80,
            "recommended_action": "DIRECT_APPLY_SAFE"
        }
        job_id = save_job(job_data)
        self.assertIsNotNone(job_id)

if __name__ == "__main__":
    unittest.main()
