#!/usr/bin/env python3
"""
Main Interactive Launcher for Angular Job Search & Referral Assistant.
"""
import sys
import os

# Ensure src/ is on python path for dynamic resolution
src_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from job_applier.main import main

if __name__ == "__main__":
    main()
