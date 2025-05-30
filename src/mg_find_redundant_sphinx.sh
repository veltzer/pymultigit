#!/bin/bash -eu
for x in py*
do
	if [ ! -d "${x}/sphinx" ]
	then
		if grep sphinx "${x}/config/python.py" > /dev/null 
		then
			echo "${x}"
		fi
	fi
done
