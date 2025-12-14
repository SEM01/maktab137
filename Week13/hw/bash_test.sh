#!/bin/bash

logmaster_dir="/home/office/Documents/Learning/project/"
log_file="report$(date +%Y-%m-%d).log"

cd "/home/office/Documents/Learning/"
source .venv/bin/activate
cd "/home/office/Documents/Learning/project"


pytest -v test_argparse.py >> "$log_file"
