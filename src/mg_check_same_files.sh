#!/bin/bash -e

tags=(*/.veltzer.tag)
folders=()
for elem in "${tags[@]}"
do
	folders+=("${elem%/*}")
done
# printf "%s\n" "${folders[@]}"

notags=([^py]*/.veltzer.tag)
nofolders=()
for elem in "${notags[@]}"
do
	nofolders+=("${elem%/*}")
done
# printf "%s\n" "${nofolders[@]}"

pytags=(py*/.veltzer.tag)
pyfolders=()
for elem in "${pytags[@]}"
do
	pyfolders+=("${elem%/*}")
done
# printf "%s\n" "${pyfolders[@]}"

function mcmp() {
	local print=$1
	local -n arr=$2
	local add=$3
	t=()
	for elem in "${arr[@]}"
	do
		if [ -f "${elem}${add}" ]
		then
			t+=("${elem}${add}")
		fi
	done
	# shellcheck disable=SC2046
	pycmdtools mcmp --print "${print}" $(printf "%s " "${t[@]}")
}
# python modules
mcmp "py*/setup.cfg" pyfolders "/setup.cfg"
mcmp "py*/Makefile" pyfolders "/Makefile"
mcmp "./*/.mypy.ini" folders "/.mypy.ini"
mcmp "./*/.pylintrc" folders "/.pylintrc"
mcmp "./*/.flake8" folders "/.flake8"
mcmp "./*/.gitignore" folders "/.gitignore"
mcmp "./*/.shellcheckrc" folders "/.shellcheckrc"
# templates
mcmp "[^py]*/templates/README.md.mako" nofolders /templates/README.md.mako
mcmp "py*/templates/LICENSE.mako" pyfolders /templates/LICENSE.mako
mcmp "py*/templates/setup.py.mako" pyfolders /templates/setup.py.mako
mcmp "py*/templates/README.rst.mako" pyfolders /templates/README.rst.mako
mcmp "py*/templates/README.md.mako" pyfolders /templates/README.md.mako
mcmp "./*/templates/.github/workflows/build.yml.mako" folders /templates/.github/workflows/build.yml.mako
mcmp "./*/templates/requirements.txt.mako" folders /templates/requirements.txt.mako
# .idea stuff
mcmp "py*/.idea/.gitignore" pyfolders /.idea/.gitignore
# results of templates
mcmp "py*/.github/workflows/build.yml" pyfolders /.github/workflows/build.yml
mcmp "[^py]*/.github/workflows/build.yml" nofolders /.github/workflows/build.yml
# github stuff
mcmp "./*/.github/FUNDING.yml" folders /.github/FUNDING.yml
# sphinx
mcmp "./*/sphinx/conf.py" folders /sphinx/conf.py
mcmp "./*/sphinx/index.rst" folders /sphinx/index.rst
# config
mcmp "./*/config/platform.py" folders /config/platform.py
mcmp "./*/config/personal.py" folders /config/personal.py
mcmp "./*/config/github.py" folders /config/github.py
# aspell
mcmp "./*/.aspell.conf" folders /config/github.py
# markdown linting with mdl
mcmp "./*/.mdlrc" folders /config/github.py
mcmp "./*/.mdl.style.rb" folders /config/github.py
