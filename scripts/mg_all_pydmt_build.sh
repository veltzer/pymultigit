#!/bin/bash -eu

# This script builds multiple git repos

for x in * 
do
	if [ ! -d "${x}" ]
	then
		continue
	fi
	echo "doing [${x}]"
	if [ ! -f "${x}/.pydmt.config" ]
	then
		# echo "no .pydmt.config"
		continue
	fi
	cd "${x}"
	# echo "building..."
	pydmt build
	cd ..
done
