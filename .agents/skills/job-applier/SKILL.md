---
name: job-applier
description: Step-by-step instructions for executing the Angular job search, scoring, cooldown defense, and referral outreach workflow.
---

# Job Applier Workflow Skill

Follow this operational workflow whenever performing job search or referral actions for the user:

1. **Auto-Initialize DB (`history.db`):** `history.db` is ignored in `.gitignore`. Run `core/history_db.py:init_db()` to automatically create SQLite tables if missing.
2. **Parse Base CV:** Read `my_cv.pdf` or `my_cv.docx` from the workspace root.
3. **Search Jobs:** Execute `python-jobspy` or call `core/job_matcher.py` for Angular Frontend roles at Product companies in India (Hybrid/WFO).
4. **Run 180-Day Cooldown Check:** Check `history.db`. If applied in last 180 days, mark `BLOCKED_COOLDOWN`.
4. **Compute Quantifiable Scores:** Calculate `Match_Score`, `Referral_Prob_Score`, and `Direct_Safety_Score`.
5. **Prompt User for 1-Word Input:** Present options (`1` = Refer Card, `2` = Direct Apply, `3` = Skip).
6. **Enforce Truthfulness:** If generating a tailored resume and missing keywords exist, prompt user for keyword approval.
7. **Format Medium-Specific Outreach:** Output referral card formatted specifically for LinkedIn, Email, Markdown, or WhatsApp.
8. **Update README.md:** Whenever requested or whenever code/workflow changes occur, update `README.md` to reflect latest setup, commands, and component summaries.
