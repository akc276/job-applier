# Project Rule: 180-Day Cooldown & Direct Apply Defense

> **Scope:** Project-Specific (Job Applier Repository)

## 180-Day Cooldown Rule
- Before taking any application action, check `history.db` for previous applications to the target company domain.
- If an application was logged within the last 180 days (6 months), mark status as `BLOCKED_COOLDOWN`.

## Direct Apply Safety Conditions
Direct application is ONLY recommended (`DIRECT_APPLY_SAFE`) if ONE of these is true:
1. **Official Policy Proof:** Career FAQ explicitly confirms short/no cooldown policy (quote & link saved to DB).
2. **Low Headcount:** Company headcount < 50 and no employee contacts can be found for referral.
3. **Single Best Fit:** No other Angular role exists at the company that better suits the profile.
