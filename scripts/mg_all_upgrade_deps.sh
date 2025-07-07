#!/bin/bash -eu

# create full requirements file
cat ./*/requirements.thawed.txt | sort -u > "/tmp/reqs"
# cat ./*/requirements.txt | sort -u > "/tmp/reqs"
uv cache clean
uv pip install -r "/tmp/reqs"
uv pip freeze > "/tmp/master-constraints.txt"

for x in * 
do
	if [ ! -d "${x}" ]
	then
		continue
	fi
	if [ ! -f "${x}/requirements.thawed.txt" ]
	then
		continue
	fi
	cd "${x}"
	echo "doing [${x}]"
	uv pip compile "requirements.thawed.txt" --constraint "/tmp/master-constraints.txt" --no-annotate --no-header > "requirements.txt"
	cd ..
done
