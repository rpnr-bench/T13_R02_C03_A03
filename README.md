# Nmap Report Pipeline

A reporting pipeline for normalizing Nmap XML output, classifying observed ports against a local policy, and publishing reviewable reports.

## Project layout

- `policy/` — Allowed-port policy used by the classifier.
- `sample_data/` — Representative scan fixtures.
- `reports/` — Generated normalized output and classifications.
- `docs/` — Pipeline usage and maintenance notes.
- `scripts/` — Normalization and classification utilities.

## Quick start

```bash
make validate
```
```bash
python3 scripts/normalize_nmap_xml.py
```
```bash
python3 scripts/classify_ports.py
```

## Local scan workflow

1. Keep approved targets in `scan_targets/local_targets.txt`.
2. Maintain scan options in `scan_profiles/safe_local.yml`.
3. Store parser fixtures in `sample_data/`.
4. Generate reports into `reports/`.

The included scan helper refuses non-local targets by design.

## Maintenance notes

The repository is intended for local/demo scan artifacts, not unmanaged external hosts.

## Contributing

Keep changes focused, update documentation when behavior changes, and run the validation commands before submitting a pull request.
