# Project Agent Instructions & Submodule Architecture

This repository uses a **Two-Tier Agent Customization System** designed for **Git Submodule Integration**.

---

## 🌐 Tier 1: Generic Global Agent Standards (`.agents/global_agent_standards/`)
*Git Submodule Candidate — Portable user standards synced across all projects.*

- [`.agents/global_agent_standards/AGENTS.md`](./global_agent_standards/AGENTS.md) - Submodule Master Entrypoint (Global Core Rules, Skills & Submodule Changelog).

---

## 🎯 Tier 2: Project-Specific Domain Rules (`.agents/project_specific/`)
*Rules specific ONLY to the Angular Job Search, Referral & Application Agent.*

- [`.agents/project_specific/angular_job_targets.md`](./project_specific/angular_job_targets.md) - Angular 14-18 targets, product company filtering, and Experience Gap Deltas.
- [`.agents/project_specific/cooldown_defense_rules.md`](./project_specific/cooldown_defense_rules.md) - 180-day SQLite cooldown defense & 3 safety rules.
- [`.agents/project_specific/outreach_channels.md`](./project_specific/outreach_channels.md) - Medium-specific formatting (LinkedIn Plaintext, Rich HTML Email, Mobile).

---

## 🛠️ Workflows & Memory Ledgers

- [`.agents/skills/job-applier/SKILL.md`](./skills/job-applier/SKILL.md) - Step-by-step operational workflow for job search & referral generation.
- [`.agents/LOGBOOK.md`](./LOGBOOK.md) - Timestamped memory ledger tracking completed tasks, remaining backlog, failed attempts, and **Decision Rationale**.

---

## 📦 Git Submodule Setup & Sync Guide
To link `.agents/global_agent_standards/` as a shared Git Submodule across your projects:

```bash
# Add submodule to any project repository:
git submodule add <YOUR_GLOBAL_STANDARDS_REPO_URL> .agents/global_agent_standards

# Pull latest global rules in any project:
git submodule update --remote --merge
```

---

## 📜 Agent Precedence & Maintenance SOP
1. **Generic Rules Primacy:** Global agent standards in `global_agent_standards/AGENTS.md` define your core AI pair-programmer persona and MUST NEVER be overridden by project code.
2. **Growing Your Global Rules:** When discovering new generic preferences, add/update them inside `global_agent_standards/` so they can be committed to your global standards repo and synced across all your projects.
3. **Logbook & README Updates:** Always update `README.md` and log timestamped session entries in `.agents/LOGBOOK.md`.
4. **Preservation of User Directives:** NEVER alter, override, or modify core user direct instructions or project specifications without asking for explicit user approval first.
5. **No Hardcoded Absolute Paths:** NEVER hardcode user-specific paths (`/Users/...`, `/home/...`) or environment identifiers in version-controlled markdown or code files.
