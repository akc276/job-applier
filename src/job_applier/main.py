#!/usr/bin/env python3
import sys
import os

# Add src to python path for standalone execution
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from job_applier.controllers.cli_controller import run_cli

def main():
    run_cli()

if __name__ == "__main__":
    main()
