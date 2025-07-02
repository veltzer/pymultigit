#!/bin/bash -eu

function old_code {
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
			uv pip install -r "requirements.txt"
		fi
		cd ..
	done
}

# create full requirements file
cat ./*/requirements.thawed.txt | sort -u > "/tmp/reqs"
uv cache clean
uv pip install -r "/tmp/reqs"
