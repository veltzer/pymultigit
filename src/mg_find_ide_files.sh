#!/bin/bash -e
find .\
	-name ".idea" -or\
	-name ".project" -or\
	-name ".settings" -or\
	-name "build.properties"
