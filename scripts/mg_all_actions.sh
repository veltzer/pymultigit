#!/bin/bash -eu

for dir in */
do
	if [[ -d "${dir}/.git" ]]
	then
		echo "🔎 Checking repository: ${dir}"
		(cd "${dir}" && gh run list --status failure --limit 5)
		echo "---------------------------------"
	fi
done
