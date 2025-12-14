#!/bin/bash

log_file="report$(date +%Y-%m-%d).log"

cd "/home/Learning/"
source .venv/bin/activate

pytest -v test_argparse.py >> "$log_file"
