#!/bin/bash -eu

for x in * 
do
	if [ ! -d "${x}" ]
	then
		continue
	fi
	cd "${x}"
	if [ -f "requirements.thawed.txt" ]
	then
		if [ ! -f "requirements.txt" ]
		then
			echo "${x}"
		fi
	fi
	cd ..
done
