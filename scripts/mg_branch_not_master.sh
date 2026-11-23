#!/bin/bash -eu
for x in *
do
	if [[ ! -d "${x}/.git" ]]
	then
		continue
	fi
	cd "${x}" || exit
	branch=$(git branch --show-current)
	if [[ "${branch}" != "master" ]]
	then
		echo "${x} local ${branch}"
	fi
	remote=$(git branch -r -q --show-current)
	if [[ "${remote}" != "master" ]]
	then
		echo "${x} remote ${branch}"
	fi
	mapfile -t branch_list < <(git branch || true)
	num_branches=${#branch_list[@]}
	if [[ "${num_branches}" != "1" ]]
	then
		echo "${x} ${num_branches}"
	fi
	cd ..
done
