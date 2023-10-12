#!/bin/bash -e
# python modules
pycmdtools mcmp --print "py*/setup.cfg" py*/setup.cfg
pycmdtools mcmp --print "py*/Makefile" py*/Makefile
pycmdtools mcmp --print "./*/.mypy.ini" ./*/.mypy.ini
pycmdtools mcmp --print "./*/.pylintrc" ./*/.pylintrc
pycmdtools mcmp --print "./*/.flake8" ./*/.flake8
pycmdtools mcmp --print "./*/.gitignore" ./*/.gitignore
pycmdtools mcmp --print "./*/.shellcheckrc" ./*/.shellcheckrc
# templates
pycmdtools mcmp --print "[^py]*/templates/README.md.mako" [^py]*/templates/README.md.mako
pycmdtools mcmp --print "py*/templates/LICENSE.mako" py*/templates/LICENSE.mako
pycmdtools mcmp --print "py*/templates/setup.py.mako" py*/templates/setup.py.mako
pycmdtools mcmp --print "py*/templates/README.rst.mako" py*/templates/README.rst.mako
pycmdtools mcmp --print "py*/templates/README.md.mako" py*/templates/README.md.mako
pycmdtools mcmp --print "py*/templates/[pkg]/static.py.mako" py*/templates/*/static.py.mako
pycmdtools mcmp --print "./*/templates/.github/workflows/build.yml.mako" ./*/templates/.github/workflows/build.yml.mako
pycmdtools mcmp --print "./*/templates/requirements.txt.mako" ./*/templates/requirements.txt.mako
# .idea stuff
pycmdtools mcmp --print "py*/.idea/.gitignore" py*/.idea/.gitignore
# results of templates
pycmdtools mcmp --print "py*/.github/workflows/build.yml" py*/.github/workflows/build.yml
pycmdtools mcmp --print "[^py]*/.github/workflows/build.yml" [^py]*/.github/workflows/build.yml
# github stuff
pycmdtools mcmp --print "./*/.github/FUNDING.yml" ./*/.github/FUNDING.yml
# sphinx
pycmdtools mcmp --print "./*/sphinx/conf.py" ./*/sphinx/conf.py
pycmdtools mcmp --print "./*/sphinx/index.rst" ./*/sphinx/index.rst
# config
pycmdtools mcmp --print "./*/config/platform.py" ./*/config/platform.py
pycmdtools mcmp --print "./*/config/personal.py" ./*/config/personal.py
pycmdtools mcmp --print "./*/config/github.py" ./*/config/github.py
