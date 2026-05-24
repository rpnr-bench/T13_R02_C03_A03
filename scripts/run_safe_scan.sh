#!/usr/bin/env bash
set -euo pipefail
TARGET=${1:-127.0.0.1}
case "$TARGET" in
  127.0.0.1|localhost) ;;
  *) echo "Refusing to scan non-local target: $TARGET" >&2; exit 2 ;;
esac
nmap -sV --top-ports 100 -oX reports/local_scan.xml "$TARGET"
