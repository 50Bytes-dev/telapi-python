#!/bin/bash
# Regenerates telapi_python from the gateway's schema, ../telapi/static/api/spec.yml.
set -euo pipefail
source .venv/bin/activate

SPEC=../telapi/static/api/spec.yml
# Hand-written modules of the package: kept across a regeneration.
KEEP=(webhooks.py)

work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT

for f in "${KEEP[@]}"; do
    if [ -f "./telapi_python/$f" ]; then cp "./telapi_python/$f" "$work/$f"; fi
done

openapi-python-client generate --custom-template-path=./templates --path "$SPEC" --overwrite --meta uv --output-path generated
rm -rf ./telapi_python
mv ./generated/telapi_client ./telapi_python
rm -rf ./generated

for f in "${KEEP[@]}"; do
    if [ -f "$work/$f" ]; then cp "$work/$f" "./telapi_python/$f"; fi
done
