# !/usr/bin/env bash

source .venv/bin/activate

black . --check --force-exclude 'build'

run check .

mypy .
