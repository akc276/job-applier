import pyperclip

def generate_mobile_referral_card(job_data, user_name="Ankit", experience_years="4+"):
    company = job_data.get("company", "the company")
    title = job_data.get("title", "Angular Frontend Developer")
    job_id = job_data.get("job_id", "N/A")
    job_url = job_data.get("job_url", "")
    
    card = f"""==================================================
  📱 REFERRAL REQUEST CARD (Ready for Mobile)
==================================================

Hi! Hope you're doing well.

I noticed an open {title} role at {company} and would be super grateful if you could refer me!

📌 TARGET DETAILS:
• Role: {title}
• Job ID: {job_id}
• Link: {job_url}
• Fallback Roles: Senior Angular Developer / Frontend Engineer (UI/UX)

⚡ QUICK SNAPSHOT (Why Me):
• {experience_years} yrs building enterprise Angular apps (RxJS, NgRx, Signals, Micro-frontends).
• Web performance specialist (Core Web Vitals +35% optimization).
• Strong TypeScript, Jasmine/Karma/Cypress, and CI/CD testing experience.

📄 RESUME:
Attached / Link: [Tailored_Angular_CV_{company.replace(' ', '_')}.pdf]

Thanks a ton for your time and help!
=================================================="""

    try:
        pyperclip.copy(card)
        copied = True
    except Exception:
        copied = False

    return card, copied
