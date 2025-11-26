import argparse
import re as regex
import os
import time

parser = argparse.ArgumentParser(
    prog="Log Analysis & Automation Toolkit",
    description="Analyze Server Logs, Extract useful information and Automate routine Operations",
    epilog="Thanks for using %(prog)s!",
)
parser.add_argument("--file", help="Log File Name")
subparsers = parser.add_subparsers(dest="Command")

# Scan Command
scan = subparsers.add_parser("scan", help="Extract all IPs")
scan_group = scan.add_mutually_exclusive_group(required=True)
scan_group.add_argument("--ip", action="store_true", help="Extract all IPs")
scan_group.add_argument("--url", action="store_true", help="Extract all URLs")
scan_group.add_argument("--errors", action="store_true", help="Detect HTTP errors")
scan.add_argument("--count", action="store_true", help="Print count of occurrences")
scan.add_argument("--export", help="Save Results to file")

# Stats Command
stats = subparsers.add_parser("stats", help="Generate Statistics")
stats.add_argument("--export", help="Save Results to file")

# Clean Command
clean = subparsers.add_parser("clean")
clean.add_argument("--rmove-ip", help="Clean logs")
clean.add_argument("--mask")
clean.add_argument("--rmove-timestamps")
clean.add_argument("--api", action="store_true")
clean.add_argument("--export")

# Monitor Command
monitor = subparsers.add_parser("monitor")
monitor.add_argument("--error", action="store_true")

args = parser.parse_args()

# REGEX PATTERNS
ip_regex = regex.compile(
    r"(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
)
url_regex = regex.compile(r"https?://[^\s]+|www\.[^\s]+")
errors_regex = regex.compile(r"\s(4\d{2}|5\d{2})\s")
api_regex = regex.compile(r'"[A-Z]+ ([^"\s]*api[^"\s/]*)', regex.IGNORECASE)
monitor_regex = regex.compile(r".*error.*", regex.IGNORECASE)

try:
    with open(args.file, "r", encoding="utf-8") as log_file:
        # log = log_file.read()
        lines = [line.rstrip("\n") for line in log_file]
except:
    print("file not found")

if args.Command == "scan":
    result = []
    count = 0
    for line in lines:
        if args.ip:
            for ip in ip_regex.findall(line):
                print(ip)
                result.append(ip)
                count += 1
        elif args.url:
            for url in url_regex.findall(line):
                print(url)
                result.append(url)
                count += 1
        elif args.errors:
            if regex.search(errors_regex, line):
                result.append(line)
                count += 1
                print(result)

        if args.count:
            print(f"Total: {count}")
        if args.export:
            with open(args.export, "w") as export_file:
                for item in result:
                    export_file.write(item + "\n")

elif args.Command == "stats":
    unique_ip = set()

    for line in lines:
        for ip in ip_regex.findall(line):
            unique_ip.add(ip)

    print(f"UNIQUE IPs: {unique_ip}")

elif args.Command == "clean":
    for line in lines:
        if args.api:
            if regex.search(api_regex, line):
                print(line)

elif args.Command == "monitor":
    for line in lines:
        if args.error:
            if regex.search(monitor_regex, line):
                print(line)
