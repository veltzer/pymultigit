#!/bin/bash -eu

shopt -s globstar
alltags=(*/.git)
allfolders=()
for elem in "${alltags[@]}"
do
	allfolders+=("${elem%/*}")
done
# printf "%s\n" "${allfolders[@]}"

tags=(*/.veltzer.tag)
myfolders=()
for elem in "${tags[@]}"
do
	myfolders+=("${elem%/*}")
done
# printf "myfolders: %s\n" "${myfolders[@]}"

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

gcptags=(gcp-*/.gcp.conf)
gcpfolders=()
for elem in "${gcptags[@]}"
do
	gcpfolders+=("${elem%/*}")
done
# printf "%s\n" "${gcpfolders[@]}"

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
mcmp "py*/Makefile" pyfolders "/Makefile"
mcmp "py*/config/deps.py" pyfolders "/config/deps.py"
mcmp "./*/.mypy.ini" allfolders "/.mypy.ini"
mcmp "./*/.pylintrc" allfolders "/.pylintrc"
mcmp "./*/.gitignore" allfolders "/.gitignore"
mcmp "./*/.shellcheckrc" allfolders "/.shellcheckrc"
mcmp "./*/.jshintrc" allfolders "/.jshintrc"
mcmp "./*/.jshintignore" allfolders "/.jshintignore"
# templates
mcmp "[^py]*/templates/README.md.mako" nofolders /templates/README.md.mako
mcmp "py*/templates/LICENSE.mako" pyfolders /templates/LICENSE.mako
# mcmp "py*/templates/setup.py.mako" pyfolders /templates/setup.py.mako
mcmp "py*/templates/pyproject.toml.mako" pyfolders /templates/pyproject.toml.mako
# mcmp "py*/templates/README.rst.mako" pyfolders /templates/README.rst.mako
mcmp "py*/templates/README.md.mako" pyfolders /templates/README.md.mako
mcmp "./*/templates/.github/workflows/build.yml.mako" allfolders /templates/.github/workflows/build.yml.mako
mcmp "./*/templates/requirements.thawed.txt.mako" allfolders /templates/requirements.thawed.txt.mako
# .idea stuff
# mcmp "py*/.idea/.gitignore" pyfolders /.idea/.gitignore
# results of templates
mcmp "py*/.github/workflows/build.yml" pyfolders /.github/workflows/build.yml
mcmp "[^py]*/.github/workflows/build.yml" nofolders /.github/workflows/build.yml
# github stuff
mcmp "./*/.github/FUNDING.yml" myfolders /.github/FUNDING.yml
# sphinx
mcmp "./*/sphinx/conf.py" myfolders /sphinx/conf.py
mcmp "./*/sphinx/index.rst" myfolders /sphinx/index.rst
# config
mcmp "./*/config/platform.py" myfolders /config/platform.py
mcmp "./*/config/personal.py" myfolders /config/personal.py
mcmp "./*/config/github.py" myfolders /config/github.py
mcmp "./*/config/shared.py" myfolders /config/shared.py
# aspell
mcmp "./*/.aspell.conf" myfolders /.aspell.conf
# markdown linting with mdl
mcmp "./*/.mdlrc" myfolders /.mdlrc
mcmp "./*/.mdl.style.rb" myfolders /.mdl.style.rb
# gcp ignore files
mcmp "gcp-*/.gcloudignore" gcpfolders /.gcloudignore
mcmp "gcp-*/Makefile" gcpfolders /Makefile
mcmp "gcp-*/app.yaml" gcpfolders /app.yaml
