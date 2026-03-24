#!/bin/bash -eux

for x in *; do
	echo "doing [${x}]"
	cd "${x}"
	git "rev-list" "--left-only" "--count" "@...@{upstream}"
	cd ".."
done
