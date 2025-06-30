#!/bin/bash -eu
for x in */Makefile
do
	echo "${x}"
	grep make_helper "${x}"
done
