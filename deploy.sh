#!/bin/sh
set -eu
cd "$(dirname "$0")"
python3 scripts/check.py
exec npx --yes wrangler@4.80.0 pages deploy site --project-name=openccman-website --branch=main
