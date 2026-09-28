#!/usr/bin/env python3
"""
Model Context Protocol (MCP) Server for Angular Job Applier Agent.
Exposes core tool capabilities to AI orchestrators.
"""
import sys
import os

src_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from job_applier.services.job_service import search_angular_jobs, evaluate_job
from job_applier.services.referral_service import generate_mobile_referral_card
from job_applier.services.resume_service import compile_typst_cv
from job_applier.repository.history_repository import check_cooldown, update_user_decision

def mcp_search_jobs(location="India", limit=5):
    """
    MCP Tool: Search Angular Frontend jobs at Product Companies with cooldown checks.
    """
    return search_angular_jobs(location=location, results_wanted=limit)

def mcp_generate_referral(job_id, company, title, job_url):
    """
    MCP Tool: Generate a mobile-formatted referral card.
    """
    job_data = {
        "id": job_id,
        "company": company,
        "title": title,
        "job_url": job_url
    }
    card, copied = generate_mobile_referral_card(job_data)
    return {"card_text": card, "copied_to_clipboard": copied}

def mcp_build_cv(company_name):
    """
    MCP Tool: Compile a customized Typst ATS CV.
    """
    pdf_path, is_compiled = compile_typst_cv(company_name)
    return {"pdf_path": pdf_path, "success": is_compiled}

def mcp_check_company_cooldown(company_name):
    """
    MCP Tool: Check if an application was logged for this company in the last 180 days.
    """
    return check_cooldown(company_name)

if __name__ == "__main__":
    print("🤖 MCP Server Module Loaded. Tools available:")
    print("  - mcp_search_jobs(location, limit)")
    print("  - mcp_generate_referral(job_id, company, title, job_url)")
    print("  - mcp_build_cv(company_name)")
    print("  - mcp_check_company_cooldown(company_name)")
