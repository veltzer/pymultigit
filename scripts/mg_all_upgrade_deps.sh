#!/bin/bash -eu

file_reqs="${VIRTUAL_ENV}/requirements.txt"
file_cons="${VIRTUAL_ENV}/master-constraints.txt"
# create full requirements file
sort -u ./*/requirements.thawed.txt > "${file_reqs}"
uv cache clean
# you can put --prerelease=disallow
uv pip install -r "${file_reqs}" --prerelease=allow
uv pip freeze > "${file_cons}"

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
	uv pip compile "requirements.thawed.txt" --constraint "${file_cons}" --no-annotate --no-header > "requirements.txt" --prerelease=allow
	cd ..
done
mg_check_collision.py
