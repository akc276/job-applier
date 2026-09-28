import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "src"))

from job_applier.services.job_service import calculate_match_score, is_product_company, calculate_experience_gaps

class TestJobService(unittest.TestCase):

    def test_calculate_match_score(self):
        score = calculate_match_score("Senior Angular Developer", "RxJS NgRx TypeScript Signals")
        self.assertGreaterEqual(score, 60)
        self.assertLessEqual(score, 98)

    def test_is_product_company(self):
        self.assertTrue(is_product_company("Swiggy"))
        self.assertTrue(is_product_company("Razorpay"))
        self.assertTrue(is_product_company("Atlassian"))
        self.assertFalse(is_product_company("Generic WITCH Agency"))

    def test_calculate_experience_gaps(self):
        gaps, health = calculate_experience_gaps("Senior Angular Developer", "Angular TypeScript RxJS")
        self.assertIsInstance(gaps, list)
        self.assertIn(health, ["🟢 GREEN", "🟡 YELLOW", "🔴 RED"])

if __name__ == "__main__":
    unittest.main()
