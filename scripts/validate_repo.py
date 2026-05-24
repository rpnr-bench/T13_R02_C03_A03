#!/usr/bin/env python3
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
required = ['README.md', 'SECURITY.md', 'scan_targets/local_targets.txt', 'scan_profiles/safe_local.yml', 'sample_data/nmap_localhost.xml', 'scripts/run_safe_scan.sh']
errors = []
for rel in required:
    if not (root / rel).exists():
        errors.append(f'missing required file: {rel}')


# Ensure local target guard exists
run_scan = (root / 'scripts' / 'run_safe_scan.sh').read_text()
if 'Refusing to scan non-local target' not in run_scan:
    errors.append('scripts/run_safe_scan.sh must reject non-local targets')

if errors:
    for error in errors:
        print(error, file=sys.stderr)
    sys.exit(1)
print('OK: T13_R02')
