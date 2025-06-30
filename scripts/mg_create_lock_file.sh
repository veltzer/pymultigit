#!/bin/bash -eu


if [ ! -f "requirements.thawed.txt" ]
then
	echo "no thawed requirements file"
	exit 1
fi
uv pip compile "requirements.thawed.txt" --no-annotate --no-header > "requirements.txt"

function old_code() {
	env_path="/tmp/venv_single"
	rm -rf "${env_path}"
	virtualenv "${env_path}"
	# shellcheck source=/dev/null
	source "${env_path}/bin/activate"
	pip install -r "requirements.thawed.txt"
	pip freeze > "requirements.txt"
	deactivate
	rm -rf "${env_path}"
}
