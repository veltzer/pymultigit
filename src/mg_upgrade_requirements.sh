#!/bin/bash -e
for x in */
do
	x=${x%*/}
	if [ ! -d "${x}/.git" ]
	then
		continue
	fi
	echo "repo [${x}]..."
	cd "${x}"
	if [ ! -f "requirements.txt" ]
	then
		cd ".."
		continue
	fi
	rm -f "requirements.txt"
	git clean -qffxd
	if ! pydmt build_venv
	then
		cd ".."
		continue
	fi
	# shellcheck source=/dev/null
	source .venv/default/bin/activate
	if ! pydmt build
	then
		deactivate
		cd ".."
		continue
	fi
	pip freeze > "requirements.txt"
	deactivate
	cd ".."
done
