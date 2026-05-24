#!/usr/bin/env python3
from pathlib import Path
import json

normalized = Path('reports/normalized_scan.json')
if not normalized.exists():
    raise SystemExit('Run scripts/normalize_nmap_xml.py first')

data = json.loads(normalized.read_text())
allowed = {8080}
rows = []
for item in data['ports']:
    label = 'allowed' if item['port'] in allowed else 'unexpected'
    rows.append(f"| {item['protocol']} | {item['port']} | {item['service']} | {label} |")

out = Path('reports/port_classification.md')
out.parent.mkdir(exist_ok=True)
out.write_text(
    '# Port Classification\n\n'
    '| Protocol | Port | Service | Label |\n'
    '| --- | --- | --- | --- |\n'
    + '\n'.join(rows) + '\n'
)
print(out)
