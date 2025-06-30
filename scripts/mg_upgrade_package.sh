#!/bin/bash -eu
for x in */
do
	x=${x%*/}
	if [ ! -d "${x}/.git" ]
	then
		continue
	fi
	echo "repo [${x}]..."
	cd "${x}"
	if [ ! -f "package-lock.json" ]
	then
		cd ".."
		continue
	fi
	if [ ! -f "package.json" ]
	then
		cd ".."
		continue
	fi
	rm -f "package-lock.json"
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
	cd ".."
done
