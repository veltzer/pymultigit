#!/bin/bash -eu

: "${VIRTUAL_ENV:?VIRTUAL_ENV must be set}"

file_cons="${VIRTUAL_ENV}/master-constraints.txt"
uv pip compile "requirements.thawed.txt" --constraint "${file_cons}" --no-annotate --no-header > "requirements.txt" --prerelease=allow
