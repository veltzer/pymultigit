#!/bin/bash -eu

function all_repos {
	for x in * 
	do
		if [ ! -d "${x}" ]
		then
			continue
		fi
		echo "doing [${x}]"
		cd "${x}"
		git_commit.sh || true
		cd ".."
	done
}

for x in $(pymultigit status --terse True)
do
	echo "doing [${x}]"
	cd "${x}"
	git_commit.sh
	cd ".."
done
