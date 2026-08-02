#!/bin/bash -eux

for x in *; do
	echo "doing [${x}]"
	if [[ ! -d "${x}" ]]; then
		continue
	fi
	cd "${x}"
	git "rev-list" "--left-only" "--count" "@...@{upstream}"
	cd ".."
done
