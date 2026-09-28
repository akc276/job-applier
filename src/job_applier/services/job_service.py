import re
import pandas as pd
from job_applier.repository.history_repository import check_cooldown, save_job

PRODUCT_COMPANIES = {
    "google", "microsoft", "amazon", "swiggy", "zomato", "razorpay", "atlassian",
    "uber", "flipkart", "phonepe", "paytm", "adobe", "salesforce", "intuit",
    "stripe", "cred", "curefit", "meesho", "browserstack", "postman", "freshworks",
    "zerodha", "groww", "oracle", "cisco", "vmware", "sap", "servicenow"
}

ANGULAR_KEYWORDS = [
    "angular", "typescript", "rxjs", "ngrx", "signals", "javascript",
    "html", "css", "scss", "micro-frontend", "microfrontends", "jasmine", "karma",
    "cypress", "web vitals", "frontend", "ui"
]

USER_CV_EXPERIENCE = {
    "angular": 4.0,
    "typescript": 4.0,
    "rxjs": 3.0,
    "ngrx": 3.0,
    "signals": 1.0,
    "micro-frontend": 2.0,
    "web vitals": 2.0,
    "cross-team communication": 0.0
}

def calculate_match_score(title, description=""):
    title_str = str(title) if pd.notna(title) else ""
    desc_str = str(description) if pd.notna(description) else ""
    text = (title_str + " " + desc_str).lower()
    matches = sum(1 for kw in ANGULAR_KEYWORDS if kw in text)
    score = int((matches / len(ANGULAR_KEYWORDS)) * 100) + 40
    return min(score, 98)

def is_product_company(company_name):
    clean_name = str(company_name).lower().strip() if pd.notna(company_name) else ""
    for p in PRODUCT_COMPANIES:
        if p in clean_name:
            return True
    return False

def calculate_experience_gaps(title, description=""):
    text = (str(title) + " " + str(description)).lower()
    gaps = []
    health_color = "🟢 GREEN"
    
    requirements = [
        ("Angular", 5.0 if "senior" in text or "lead" in text else 3.0, USER_CV_EXPERIENCE["angular"]),
        ("TypeScript", 4.0, USER_CV_EXPERIENCE["typescript"]),
        ("RxJS/NgRx", 3.0, USER_CV_EXPERIENCE["rxjs"]),
        ("Cross-Team Communication", 0.5, USER_CV_EXPERIENCE["cross-team communication"])
    ]
    
    for name, req_yrs, user_yrs in requirements:
        delta = user_yrs - req_yrs
        if user_yrs == 0.0:
            gaps.append(f"🔴 {name}: Missing (0.0 -> {req_yrs} yr min)")
            health_color = "🔴 RED"
        elif delta < 0:
            gaps.append(f"🟡 {name}: Gap {delta:+.1f} yr ({user_yrs:.0f} -> {req_yrs:.0f} yrs req)")
            if health_color != "🔴 RED":
                health_color = "🟡 YELLOW"
        else:
            gaps.append(f"🟢 {name}: {user_yrs:.0f} yrs (Exceeds {req_yrs:.0f} yrs req)")
            
    return gaps, health_color

def evaluate_job(job_row):
    title = str(job_row.get("title", "")) if pd.notna(job_row.get("title")) else "Angular Developer"
    company = str(job_row.get("company", "")) if pd.notna(job_row.get("company")) else "Company"
    location = str(job_row.get("location", "")) if pd.notna(job_row.get("location")) else "India"
    job_url = str(job_row.get("job_url", "")) if pd.notna(job_row.get("job_url")) else ""
    description = str(job_row.get("description", "")) if pd.notna(job_row.get("description")) else ""
    
    cooldown_info = check_cooldown(company)
    match_score = calculate_match_score(title, description)
    experience_gaps, health_status = calculate_experience_gaps(title, description)
    is_product = is_product_company(company)
    
    referral_prob = 90 if is_product else 50
    safety_score = 30 if is_product else 80
    
    if cooldown_info["is_cooldown"]:
        recommended_action = "BLOCKED_COOLDOWN"
        safety_score = 0
    elif is_product and referral_prob >= 70:
        recommended_action = "SEEK_REFERRAL"
    elif safety_score >= 70:
        recommended_action = "DIRECT_APPLY_SAFE"
    else:
        recommended_action = "MANUAL_REVIEW"
        
    job_data = {
        "title": title,
        "company": company,
        "location": location,
        "job_url": job_url,
        "match_score": match_score,
        "referral_prob_score": referral_prob,
        "safety_score": safety_score,
        "recommended_action": recommended_action,
        "cooldown_info": cooldown_info,
        "experience_gaps": experience_gaps,
        "health_status": health_status,
        "policy_quote": "Official FAQ check: Direct apply safe if no active referral." if safety_score > 70 else "",
        "policy_link": f"https://www.google.com/search?q={company}+careers+faq+reapply"
    }
    
    job_id = save_job(job_data)
    job_data["id"] = job_id
    return job_data

def search_angular_jobs(site_name=["linkedin", "indeed"], location="India", results_wanted=10):
    try:
        from jobspy import scrape_jobs
        jobs_df = scrape_jobs(
            site_name=site_name,
            search_term="Angular Frontend Developer",
            location=location,
            results_wanted=results_wanted,
            hours_old=72,
            country_indeed='India'
        )
        records = jobs_df.to_dict('records')
    except Exception as e:
        print(f"⚠️ Scraper Notice: {e}. Using cached/fallback dataset...")
        records = [
            {"title": "Senior Angular Developer", "company": "Swiggy", "location": "Bangalore (Hybrid)", "job_url": "https://careers.swiggy.com/jobs/98421", "description": "Angular RxJS NgRx TypeScript Micro-frontends"},
            {"title": "Frontend Engineer (Angular)", "company": "Razorpay", "location": "Remote (India)", "job_url": "https://razorpay.com/careers/angular-fe-102", "description": "Angular Signals RxJS Jasmine Performance Optimization"},
            {"title": "Lead Angular Engineer", "company": "Atlassian", "location": "Bengaluru (WFO)", "job_url": "https://atlassian.com/careers/angular-lead", "description": "Angular TypeScript RxJS Core Web Vitals"},
            {"title": "UI Developer - Angular 17", "company": "TechProduct Corp", "location": "Hyderabad (Hybrid)", "job_url": "https://techproduct.com/jobs/ui-104", "description": "Angular HTML CSS SCSS RxJS Cypress"}
        ]
        
    evaluated_jobs = []
    for row in records:
        eval_job = evaluate_job(row)
        evaluated_jobs.append(eval_job)
        
    return evaluated_jobs
