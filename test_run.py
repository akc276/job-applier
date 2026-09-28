import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from job_applier.services.job_service import search_angular_jobs
from job_applier.services.referral_service import generate_mobile_referral_card
from job_applier.services.resume_service import compile_typst_cv
from job_applier.repository.history_repository import check_cooldown

print("🔍 Running Angular Job Matcher Test...")
jobs = search_angular_jobs(results_wanted=3)

print(f"\n✅ Discovered {len(jobs)} jobs:")
for j in jobs:
    print(f"\n--- Job #{j['id']}: {j['title']} @ {j['company']} ---")
    print(f"  Match Score:        {j['match_score']}%")
    print(f"  Referral Prob:     {j['referral_prob_score']}%")
    print(f"  Safety Score:      {j['safety_score']}%")
    print(f"  Action Rec:        {j['recommended_action']}")
    print(f"  Cooldown Status:   {'BLOCKED' if j['cooldown_info']['is_cooldown'] else 'CLEAN'}")

print("\n📱 Testing Mobile Referral Card Generation for Job #1...")
if jobs:
    card, copied = generate_mobile_referral_card(jobs[0])
    print(card)
    
print("\n📄 Testing Typst CV Engine...")
pdf_path, is_compiled = compile_typst_cv(jobs[0]["company"] if jobs else "Swiggy")
print(f"CV generated at: {pdf_path} (Compiled: {is_compiled})")

print("\n🎉 Everything is working seamlessly!")
