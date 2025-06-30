#!/bin/bash -eu

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
	rm -rf "/tmp/venv"
	virtualenv "/tmp/venv"
	# shellcheck source=/dev/null
	source "/tmp/venv/bin/activate"
	pip install -r "requirements.thawed.txt"
	pip freeze > "requirements.txt"
	deactivate
	rm -rf "/tmp/venv"
	cd ..
done
