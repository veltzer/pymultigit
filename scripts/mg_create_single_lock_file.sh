#!/bin/bash -eu

rm -rf /tmp/venv
virtualenv /tmp/venv
source /tmp/.venv/bin/activate
pip install -r requirements.thawed.txt
pip freeze > requirements.txt
deactivate
rm -rf /tmp/venv
