import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "src"))

from job_applier.services.job_service import evaluate_job
from job_applier.services.referral_service import generate_mobile_referral_card
from job_applier.services.resume_service import compile_typst_cv

class TestSystemIntegration(unittest.TestCase):

    def test_end_to_end_flow(self):
        # 1. Evaluate job
        job_row = {
            "title": "Lead Angular Developer",
            "company": "Atlassian",
            "location": "Bengaluru",
            "job_url": "https://atlassian.com/jobs/999",
            "description": "Angular RxJS NgRx Signals TypeScript Microfrontends"
        }
        evaluated = evaluate_job(job_row)
        self.assertEqual(evaluated["company"], "Atlassian")
        self.assertGreater(evaluated["match_score"], 60)

        # 2. Generate referral card
        card_text, copied = generate_mobile_referral_card(evaluated)
        self.assertIn("Atlassian", card_text)

        # 3. Compile CV
        cv_path, is_compiled = compile_typst_cv("Atlassian")
        self.assertTrue(os.path.exists(cv_path))

if __name__ == "__main__":
    unittest.main()
