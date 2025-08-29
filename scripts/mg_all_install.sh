#!/bin/bash -eu

# This script runs over multiple git repos installing the requirements they
# need into a single git repo

for x in * 
do
	if [ ! -d "${x}" ]
	then
		continue
	fi
	echo "doing [${x}]"
	cd "${x}"
	if [ -f "requirements.txt" ]
	then
		if [ -s "requirements.txt" ]
		then
			uv pip install --strict -r "requirements.txt"
		else
			echo "ERROR: requirements.txt file is empty!"
			exit 1
		fi
	fi
	cd ..
done
