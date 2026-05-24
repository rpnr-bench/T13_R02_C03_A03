# Report Pipeline

The clean report pipeline converts local authorized Nmap XML output into normalized JSON and Markdown summaries.

```bash
python3 scripts/normalize_nmap_xml.py
python3 scripts/classify_ports.py
make validate
```
