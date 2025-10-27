#!/bin/bash -eu

file_cons="${VIRTUAL_ENV}/master-constraints.txt"
uv pip compile "requirements.thawed.txt" --constraint "${file_cons}" --no-annotate --no-header > "requirements.txt" --prerelease=allow
