#!/bin/bash -e
for x in "$@"
do
	if [ ! -d "${x}/.git" ]
	then
		continue
	fi
	echo "repo [${x}]..."
	cd "${x}" || exit
	if [ ! -f "requirements.txt" ]
	then
		cd ".."
		continue
	fi
	rm -f "requirements.txt"
	git clean -qffxd
	pydmt build_venv
	# shellcheck source=/dev/null
	source .venv/default/bin/activate
	pydmt build
	pip freeze > "requirements.txt"
	deactivate
	cd ..
done
