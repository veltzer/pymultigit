#!/bin/bash -e
find .\
	-name ".idea" -or\
	-name ".project" -or\
	-name ".settings" -or\
	-name ".classpath" -or\
	-name "build.properties" | grep -v gems | grep -v node_modules
