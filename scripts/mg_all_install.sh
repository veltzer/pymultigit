#!/bin/bash -eu

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
		pip install -r "requirements.txt"
	fi
	cd ..
done
