import sqlite3
import os
from datetime import datetime, timedelta
import re

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), "data", "local")
DB_PATH = os.path.join(DATA_DIR, "history.db")

def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR, exist_ok=True)

def init_db():
    ensure_data_dir()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_title TEXT NOT NULL,
            company TEXT NOT NULL,
            company_domain TEXT NOT NULL,
            location TEXT,
            job_url TEXT UNIQUE,
            match_score INTEGER,
            referral_prob_score INTEGER,
            safety_score INTEGER,
            recommended_action TEXT,
            status TEXT DEFAULT 'DISCOVERED',
            user_decision TEXT DEFAULT 'PENDING',
            policy_quote TEXT,
            policy_link TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def normalize_domain(company_name):
    clean = re.sub(r'[^a-zA-Z0-9]', '', str(company_name).lower())
    return clean

def check_cooldown(company_name, cooldown_days=180):
    init_db()
    domain = normalize_domain(company_name)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cutoff_date = (datetime.now() - timedelta(days=cooldown_days)).strftime('%Y-%m-%d %H:%M:%S')
    
    cursor.execute("""
        SELECT job_title, status, created_at FROM applications
        WHERE company_domain = ? AND created_at >= ?
        ORDER BY created_at DESC LIMIT 1
    """, (domain, cutoff_date))
    
    result = cursor.fetchone()
    conn.close()
    
    if result:
        last_title, status, created_at = result
        created_dt = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
        days_ago = (datetime.now() - created_dt).days
        days_remaining = cooldown_days - days_ago
        return {
            "is_cooldown": True,
            "last_title": last_title,
            "status": status,
            "days_remaining": days_remaining,
            "applied_at": created_at
        }
    return {"is_cooldown": False, "days_remaining": 0}

def save_job(job_data):
    init_db()
    domain = normalize_domain(job_data.get("company", ""))
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO applications (
                job_title, company, company_domain, location, job_url,
                match_score, referral_prob_score, safety_score,
                recommended_action, status, policy_quote, policy_link
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            job_data.get("title"),
            job_data.get("company"),
            domain,
            job_data.get("location"),
            job_data.get("job_url"),
            job_data.get("match_score", 0),
            job_data.get("referral_prob_score", 0),
            job_data.get("safety_score", 0),
            job_data.get("recommended_action", "MANUAL_REVIEW"),
            "DISCOVERED",
            job_data.get("policy_quote", ""),
            job_data.get("policy_link", "")
        ))
        conn.commit()
        job_id = cursor.lastrowid
    except sqlite3.IntegrityError:
        cursor.execute("SELECT id FROM applications WHERE job_url = ?", (job_data.get("job_url"),))
        row = cursor.fetchone()
        job_id = row[0] if row else None
    finally:
        conn.close()
    return job_id

def update_user_decision(job_id, decision, status=None):
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    if status:
        cursor.execute("""
            UPDATE applications 
            SET user_decision = ?, status = ?, updated_at = ?
            WHERE id = ?
        """, (decision, status, updated_at, job_id))
    else:
        cursor.execute("""
            UPDATE applications 
            SET user_decision = ?, updated_at = ?
            WHERE id = ?
        """, (decision, updated_at, job_id))
        
    conn.commit()
    conn.close()

init_db()
