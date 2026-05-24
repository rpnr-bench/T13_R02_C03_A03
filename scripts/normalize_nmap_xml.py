#!/usr/bin/env python3
from pathlib import Path
import json
import xml.etree.ElementTree as ET

src = Path('sample_data/nmap_sample.xml')
out = Path('reports/normalized_scan.json')
out.parent.mkdir(exist_ok=True)
root = ET.parse(src).getroot()
ports = []
for port in root.findall('.//port'):
    state_el = port.find('state')
    service_el = port.find('service')
    ports.append({
        'protocol': port.attrib.get('protocol'),
        'port': int(port.attrib.get('portid')),
        'state': state_el.attrib.get('state') if state_el is not None else 'unknown',
        'service': service_el.attrib.get('name') if service_el is not None else 'unknown',
    })
out.write_text(json.dumps({'target': '127.0.0.1', 'ports': ports}, indent=2) + '\n')
print(out)
