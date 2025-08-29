#!/bin/bash -eu

# create full requirements file
cat ./*/requirements.thawed.txt | sort -u > "/tmp/requirements.txt"
uv cache clean
# uv pip install -r "/tmp/requirements.txt" --prerelease=disallow
uv pip install -r "/tmp/requirements.txt" --prerelease=allow
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
	uv pip compile "requirements.thawed.txt" --constraint "/tmp/master-constraints.txt" --no-annotate --no-header > "requirements.txt" --prerelease=allow
	cd ..
done
mg_check_collision.py
