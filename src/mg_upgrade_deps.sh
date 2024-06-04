#!/bin/bash -e
# for x in "$@"
for x in *
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
	if pydmt build_venv
	then
		# shellcheck source=/dev/null
		source .venv/default/bin/activate
		if pydmt build
		then
			pip freeze > "requirements.txt"
		fi
		deactivate
	fi
	cd ".."
done
