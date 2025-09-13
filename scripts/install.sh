#!/bin/bash


echo "Installing project dependencies with poetry..."
poetry install

echo "Installing the package in editable mode..."
poetry install -E dev
