# Agent Execution Logbook & Memory Ledger

This file tracks **timestamped progress**, **decision rationale (why we built/changed/abandoned things)**, **failed attempts**, and **chronological change history** across session executions.

---

## 🚦 Active Roadmap & Timestamped Progress

### ✅ Completed Milestones
- `[2026-09-29 02:19 IST]` **Git Submodule & Repository Setup:** Linked remote repositories `github.com/akc276/global-agent-standards.git` and `github.com/akc276/job-applier.git` with initial commit status noted as *Not tested by human yet*.
- `[2026-09-29 02:11 IST]` **Submodule Self-Containment:** Added dedicated `AGENTS.md`, `LOGBOOK.md`, `rules/`, and `skills/` directories to make `global_agent_standards` a 100% self-contained Git Submodule repository.
- `[2026-09-29 02:06 IST]` **Pytest Standard & Tech Transition Protocol:** Standardized `pytest` runner and added major framework transition protocol.
- `[2026-09-29 02:02 IST]` **Modular `src/` Packaging Layout & Tests:** Refactored project into `src/job_applier/controllers/`, `services/`, `repository/`, and `tests/` with 100% unit & integration test coverage.
- `[2026-09-29 01:59 IST]` **Git Repository Initialized:** Initialized empty Git repository (`.git`).
- `[2026-09-29 01:53 IST]` **Two-Tier Agent Standards:** Separated `.agents/global_agent_standards/` (portable) from `.agents/project_specific/`.
- `[2026-09-29 01:44 IST]` **Git & Venv Hygiene:** Hidden `.venv` virtual environment setup, `data/local/` data separation, and `.gitignore` configuration.
- `[2026-09-29 01:35 IST]` **Skill & Experience Gap Analysis:** Explicit deltas (`Angular: 4 yrs vs 5 yrs req (-1 yr gap)`) with 🟢/🟡/🔴 indicators and interactive `g [Job ID]` CLI inspector.
- `[2026-09-29 00:55 IST]` **Phase 1 MVP:** Interactive CLI (`app.py`) for live Angular job search & scoring.

### ⏳ Remaining Backlog (Upcoming Phases)
- [ ] **Phase 2 (Keyword Approval Guard):** CLI prompt asking user approval (`[y/n]`) before adding missing keywords to CV.
- [ ] **Phase 3 (Medium-Specific Outreach Generator):** Automatic HTML Email, LinkedIn Plaintext, and Markdown generator options.
- [ ] **Phase 4 (Playwright ATS Form Auto-Filler):** Greenhouse & Lever form filler with human confirmation step.
- [ ] **Phase 5 (FastMCP Server Integration):** Expose tools via MCP SDK for autonomous agent execution.

---

## 💡 Decision Rationale, Plans & Abandoned Approaches Log

| Timestamp (IST) | Decision / Pivot | Original Plan | New Approach / Why Pivoted | User Preference Reason |
| :--- | :--- | :--- | :--- | :--- |
| **2026-09-29 02:19** | **Remote Git Submodule Linking (`akc276`)** | Local-only repository setup. | Initialize submodule git repo in `.agents/global_agent_standards` pointing to `github.com/akc276/global-agent-standards.git` and host repo to `github.com/akc276/job-applier.git`. | User wants to maintain global standards in a central GitHub repository across all projects. |
| **2026-09-29 02:09** | **Git Submodule Architecture for Global Rules** | Nested `.agents/rules/global_agent_standards/` subfolder. | Top-level `.agents/global_agent_standards/` directory. | Allows user to link `.agents/global_agent_standards/` directly as a single Git Submodule across all current & future repos. |
| **2026-09-29 02:06** | **`pytest` Standard & Tech Transition Protocol** | `unittest` runner. | Adopt `pytest` as standard test framework; add requirement to prompt user for framework choices on major tech stack changes. | User prefers `pytest` for Python projects and explicit suggestions on major framework pivots. |

---

## 📜 Timestamped Attempt History & Failed Experiment Log

| Timestamp (IST) | Issue / Experiment | Root Cause | Resolution / Fix |
| :--- | :--- | :--- | :--- |
| **2026-09-29 02:19** | Setting up remote git submodules for `akc276`. | `.agents/global_agent_standards` was an uninitialized folder inside the host repo. | Ran `git init`, committed files, and set remote origin to `github.com/akc276/global-agent-standards.git`. |

---

## 📅 Chronological Change Journal

- **`[2026-09-29 02:19 IST]` Configured Git Submodule Remote Links for `akc276`**
  - Updated `README.md` with Status Note disclaimer (*Not tested by human yet*).
  - Initialized git repository inside `.agents/global_agent_standards/` and linked remote `https://github.com/akc276/global-agent-standards.git`.
  - Linked host repository remote `https://github.com/akc276/job-applier.git`.
