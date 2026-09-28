# Angular Job Search, Referral & Application Agent

An automated, safety-first job search assistant and referral card generator specifically tailored for **Angular Frontend Developers** targeting **Product-Based Companies** (Hybrid / WFO priority).

> ⚠️ **Status Note:** Initial system architecture, CLI dashboard, scoring engine, and unit/integration test suite created. **Not fully tested end-to-end by human yet.**

---

## ⚡ Quick Start & Setup

### 1. Prerequisites
- Python 3.11+
- Git

### 2. Installation
```bash
# Clone or navigate to project directory
cd job-applier

# Create virtual environment and install dependencies
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
```

### 3. How to Run the App
Launch the interactive CLI dashboard:
```bash
./.venv/bin/python app.py
```

### 4. How to Run Test Suite
Run unit & integration tests via `pytest`:
```bash
# Run all tests
./.venv/bin/pytest tests

# Run unit tests only
./.venv/bin/pytest tests/unit

# Run integration tests only
./.venv/bin/pytest tests/integration
```

---

## 💡 Quick Command Options in `app.py`

When you run `./.venv/bin/python app.py`, you can enter 1-word commands:
- `1 [Job ID]` → Generate Mobile Referral Card & Copy to Clipboard
- `2 [Job ID]` → Mark for Safe Direct Apply
- `3 [Job ID]` → Skip Job
- `g [Job ID]` → View Quantified Skill & Experience Gap Breakdown
- `4`          → Export all listings to Excel (`data/local/job_tracker.xlsx`)
- `r`          → Refresh / Search Again
- `q`          → Quit

---

## 🧱 Modular Packaging Architecture (`src/` Layout)

```text
job-applier/
├── src/
│   └── job_applier/
│       ├── main.py                             # Core application entrypoint
│       ├── controllers/
│       │   └── cli_controller.py               # Terminal UI & 1-word command handler
│       ├── services/
│       │   ├── job_service.py                  # Job search, match scoring & gap analysis
│       │   ├── referral_service.py             # Mobile referral card generator
│       │   └── resume_service.py               # ATS CV compilation engine
│       └── repository/
│           └── history_repository.py           # SQLite database persistence & cooldown check
├── tests/
│   ├── unit/                                   # Unit test suite (7 tests)
│   └── integration/                            # Integration test suite (1 test)
├── data/
│   └── local/                                  # Local DB (history.db) & Excel exports (git-ignored)
├── templates/
│   └── cv_template.typ                         # ATS CV template
├── .agents/                                    # Agent Guidelines & Memory Ledgers
│   ├── AGENTS.md                               # Host Project Master Entrypoint
│   ├── LOGBOOK.md                              # Host Project Memory Ledger
│   ├── global_agent_standards/                  # 🌐 STANDALONE GIT SUBMODULE REPOSITORY
│   │   ├── AGENTS.md                           # Submodule Master Instructions
│   │   ├── LOGBOOK.md                          # Submodule Revision Ledger
│   │   ├── rules/                              # Shared Global Rules
│   │   └── skills/                             # Shared Global Skills (e.g. repo-initializer)
│   ├── project_specific/                        # 🎯 Host Project Rules
│   └── skills/                                 # Host Project Skills
├── AGENTS.md                                   # Root Agent Instruction Pointer
├── app.py                                      # Interactive CLI Launcher
├── mcp_server.py                               # FastMCP Server Entrypoint
├── test_run.py                                 # E2E System Test Script
├── requirements.txt                            # Dependency manifest
├── .gitignore                                  # Git exclusion rules
└── README.md                                   # Project Documentation
```

---

## 🛡️ Core Rules & Policies (`.agents/`)

- **180-Day Cooldown Defense:** Prevents applying twice to the same company within 6 months.
- **Quantifiable Skill & Experience Gap Analysis:** Explicitly computes experience deltas with color indicators (🟢 Green, 🟡 Yellow, 🔴 Red).
- **Truthful Resume Guard:** Never fabricates skills. Prompts user for approval before adding unmentioned JD keywords.
- **Medium-Specific Formatting:** Tailors outreach text specifically for LinkedIn Plaintext, Rich HTML Email, Markdown, or WhatsApp.
