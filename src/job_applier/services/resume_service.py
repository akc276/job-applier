import os
import subprocess
import shutil

TEMPLATE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), "templates", "cv_template.typ")
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), "data", "local", "output")

def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR, exist_ok=True)

def compile_typst_cv(company_name="Company"):
    ensure_output_dir()
    clean_co_name = "".join(c for c in company_name if c.isalnum() or c in (' ', '_')).replace(' ', '_')
    out_pdf_path = os.path.join(OUTPUT_DIR, f"cv_Angular_{clean_co_name}.pdf")
    
    typst_bin = shutil.which("typst")
    if typst_bin:
        try:
            cmd = [typst_bin, "compile", TEMPLATE_PATH, out_pdf_path]
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return out_pdf_path, True
        except Exception as e:
            print(f"Typst compile warning: {e}")
            
    fallback_path = os.path.join(OUTPUT_DIR, f"cv_Angular_{clean_co_name}.txt")
    shutil.copyfile(TEMPLATE_PATH, fallback_path)
    return fallback_path, False
