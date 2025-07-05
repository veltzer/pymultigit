#!/bin/bash -eu

# This script will do some "cross project" linting

# check that package.json files do not have number in them (they should have "latest")
grep -E "[0-9]" ./*/package.json
