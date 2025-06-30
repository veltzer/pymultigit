#!/bin/bash -eu

for x in * 
do
	if [ ! -d "${x}" ]
	then
		continue
	fi
	echo "doing [${x}]"
	cd "${x}"
	mg_create_lock_file.sh
	cd ..
done
