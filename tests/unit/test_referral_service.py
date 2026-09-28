import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "src"))

from job_applier.services.referral_service import generate_mobile_referral_card

class TestReferralService(unittest.TestCase):

    def test_generate_referral_card(self):
        job_data = {
            "title": "Angular Specialist",
            "company": "Swiggy",
            "job_id": "SWG-101",
            "job_url": "https://swiggy.com/jobs/101"
        }
        card, copied = generate_mobile_referral_card(job_data)
        self.assertIn("Swiggy", card)
        self.assertIn("Angular Specialist", card)
        self.assertIsInstance(copied, bool)

if __name__ == "__main__":
    unittest.main()
