#!/bin/bash -eu
for x in py*
do
	if [ ! -f "${x}/MANIFEST.in" ]
	then
		echo "${x}"
	fi
done
