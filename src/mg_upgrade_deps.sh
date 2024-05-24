#!/bin/bash -e
for x in *
do
	if [ ! -d "${x}/.git" ]
	then
		continue
	fi
	cd "${x}" || exit
	if [ ! -f "requirements.txt" ]
	then
		cd ".."
		continue
	fi
	rm -f "requirements.txt"
	make clean_hard
	prompt_pydmt
	pydmt_build
	pip freeze > "requirements.txt"
	cd ..
done
