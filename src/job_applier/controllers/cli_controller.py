import os
import pandas as pd
from tabulate import tabulate

from job_applier.services.job_service import search_angular_jobs
from job_applier.services.referral_service import generate_mobile_referral_card
from job_applier.repository.history_repository import update_user_decision

def print_banner():
    print("""
========================================================================
  🚀 ANGULAR JOB APPLIER & REFERRAL AGENT (Modular MVC Layout)
  Safety-First | 180-Day Cooldown Defense | Mobile Referral Generator
========================================================================
""")

def display_job_table(jobs):
    table_data = []
    for j in jobs:
        cooldown_str = f"BLOCKED ({j['cooldown_info']['days_remaining']}d left)" if j['cooldown_info']['is_cooldown'] else "CLEAN"
        health_str = j.get("health_status", "🟢 GREEN")
        table_data.append([
            j["id"],
            j["company"][:15],
            j["title"][:22],
            f"{j['match_score']}%",
            f"{j['referral_prob_score']}%",
            f"{j['safety_score']}%",
            health_str,
            cooldown_str,
            j["recommended_action"]
        ])
    
    headers = ["ID", "Company", "Job Title", "Match", "Ref Prob", "Safety", "Health", "Cooldown", "Recommended Action"]
    print("\n" + tabulate(table_data, headers=headers, tablefmt="fancy_grid") + "\n")

def display_experience_gaps(job):
    print(f"\n📊 EXPERIENCE & SKILL GAP ANALYSIS for Job #{job['id']} (@ {job['company']}):")
    print("=" * 65)
    for line in job.get("experience_gaps", []):
        print(f"  {line}")
    print("=" * 65 + "\n")

def export_to_excel(jobs):
    data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), "data", "local")
    os.makedirs(data_dir, exist_ok=True)
    excel_path = os.path.join(data_dir, "job_tracker.xlsx")
    df = pd.DataFrame(jobs)
    df.to_excel(excel_path, index=False)
    print(f"📊 Exported {len(jobs)} job listings to: {excel_path}")

def run_cli():
    print_banner()
    print("🔍 Fetching live Angular Frontend jobs for Product-Based Companies...")
    jobs = search_angular_jobs(results_wanted=5)
    job_map = {j["id"]: j for j in jobs}
    
    while True:
        display_job_table(jobs)
        print("💡 QUICK COMMAND OPTIONS:")
        print("  1 [Job ID] -> Generate Mobile Referral Card & Copy to Clipboard")
        print("  2 [Job ID] -> Mark for Safe Direct Apply")
        print("  3 [Job ID] -> Skip Job")
        print("  g [Job ID] -> View Quantified Skill & Experience Gap Breakdown")
        print("  4          -> Export All to Excel (data/local/job_tracker.xlsx)")
        print("  r          -> Refresh / Search Again")
        print("  q          -> Quit")
        
        user_input = input("\n👉 Enter command (e.g., '1 1' or '4'): ").strip()
        
        if user_input.lower() == 'q':
            print("👋 Bye! Good luck with your applications!")
            break
        elif user_input.lower() == 'r':
            print("🔄 Refreshing job listings...")
            jobs = search_angular_jobs(results_wanted=5)
            job_map = {j["id"]: j for j in jobs}
            continue
        elif user_input == '4':
            export_to_excel(jobs)
            continue
            
        parts = user_input.split()
        if len(parts) == 2:
            cmd, target_id_str = parts[0], parts[1]
            try:
                target_id = int(target_id_str)
                if target_id in job_map:
                    job = job_map[target_id]
                    if cmd == '1':
                        card_text, copied = generate_mobile_referral_card(job)
                        update_user_decision(target_id, "REFERRAL_CARD_GENERATED", status="REFERRAL_PENDING")
                        print("\n" + card_text + "\n")
                        if copied:
                            print("✅ SUCCESS: Mobile Referral Card COPIED to your clipboard! Ready to paste into LinkedIn/WhatsApp.")
                        else:
                            print("📋 Copy the card above to send to your referral contact!")
                    elif cmd == '2':
                        update_user_decision(target_id, "DIRECT_APPLY_APPROVED", status="QUEUED_FOR_APPLY")
                        print(f"✅ Job #{target_id} (@ {job['company']}) queued for Safe Direct Apply!")
                    elif cmd == '3':
                        update_user_decision(target_id, "SKIPPED", status="IGNORED")
                        print(f"🙈 Job #{target_id} marked as Skipped.")
                    elif cmd.lower() == 'g':
                        display_experience_gaps(job)
                    else:
                        print("⚠️ Unknown command option. Use 1, 2, 3, or g followed by Job ID.")
                else:
                    print("⚠️ Invalid Job ID. Please choose an ID from the table.")
            except ValueError:
                print("⚠️ Please enter a numeric Job ID (e.g. '1 1').")
        else:
            print("⚠️ Invalid format. Type '1 1' to get referral card for Job ID 1, or 'q' to quit.")
