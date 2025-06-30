#!/bin/bash -eu

if [ ! -f "requirements.thawed.txt" ]
then
	echo "no thawed requirements file"
	exit 1
fi
rm -rf "/tmp/venv"
virtualenv "/tmp/venv"
# shellcheck source=/dev/null
source "/tmp/venv/bin/activate"
pip install -r "requirements.thawed.txt"
pip freeze > "requirements.txt"
deactivate
rm -rf "/tmp/venv"
