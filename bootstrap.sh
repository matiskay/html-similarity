#!/bin/bash

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "Error: uv is not installed. Please install it first."
    echo "You can install it using: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Creating new virtual environment..."
else
    echo "Using existing virtual environment..."
fi

uv sync --group dev
source .venv/bin/activate
