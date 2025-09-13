#!/bin/bash
set -e

source .venv/bin/activate

echo "Running tests..."
poetry run pytest
