#!/bin/bash
set -e

echo "Building Sphinx documentation..."
poetry run sphinx-build -b html docs docs/_build/html

echo "Docs built at docs/_build/html/index.html"
