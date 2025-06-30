#!/bin/bash -eu

env_path="/tmp/venv_single"

if [ ! -f "requirements.thawed.txt" ]
then
	echo "no thawed requirements file"
	exit 1
fi
rm -rf "${env_path}"
virtualenv "${env_path}"
# shellcheck source=/dev/null
source "${env_path}/bin/activate"
pip install -r "requirements.thawed.txt"
pip freeze > "requirements.txt"
deactivate
rm -rf "${env_path}"
