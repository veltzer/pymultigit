#!/bin/bash -eu

function old_code() {
	env_path="/tmp/venv_all"
	# this is the old code
	rm -rf "${env_path}"
	virtualenv "${env_path}"
	# shellcheck source=/dev/null
	source "${env_path}/bin/activate"
	pip install -r "requirements.thawed.txt"
	pip freeze > "requirements.txt"
	deactivate
	rm -rf "${env_path}"
}

for x in * 
do
	if [ ! -d "${x}" ]
	then
		continue
	fi
	if [ ! -f "${x}/requirements.thawed.txt" ]
	then
		continue
	fi
	cd "${x}"
	echo "doing [${x}]"
	uv pip compile "requirements.thawed.txt" --no-annotate --no-header --output-file "requirements.txt"
	cd ..
done
