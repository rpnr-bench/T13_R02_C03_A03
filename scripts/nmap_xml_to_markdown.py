#!/usr/bin/env python3
from pathlib import Path
import xml.etree.ElementTree as ET

src = Path('sample_data/nmap_localhost.xml')
out = Path('reports/local_scan_report.md')
out.parent.mkdir(exist_ok=True)
root = ET.parse(src).getroot()
rows = []
for port in root.findall('.//port'):
    portid = port.attrib.get('portid')
    proto = port.attrib.get('protocol')
    state_el = port.find('state')
    service_el = port.find('service')
    state = state_el.attrib.get('state') if state_el is not None else 'unknown'
    service = service_el.attrib.get('name') if service_el is not None else 'unknown'
    rows.append(f'| {proto} | {portid} | {state} | {service} |')
out.write_text(
    '# Local Scan Report\n\n'
    '| Protocol | Port | State | Service |\n'
    '| --- | --- | --- | --- |\n'
    + '\n'.join(rows) + '\n'
)
print(out)
