#!/bin/bash -eu

for x in * 
do
	if [ ! -d "${x}" ]
	then
		continue
	fi
	if [ ! -f "pydmt.config" ]
	then
		continue
	fi
	echo "doing [${x}]"
	cd "${x}"
	pydmt build
	cd ..
done
