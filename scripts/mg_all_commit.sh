#!/bin/bash -eu

for x in * 
do
	if [ ! -d "${x}" ]
	then
		continue
	fi
	echo "doing [${x}]"
	cd "${x}"
	git_commit.sh || true
	cd ..
done
