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
	if [ ! -f "Gemfile.lock" ]
	then
		cd ".."
		continue
	fi
	if [ ! -f "Gemfile" ]
	then
		cd ".."
		continue
	fi
	rm -f "Gemfile.lock"
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
