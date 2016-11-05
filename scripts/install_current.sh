#!/bin/sh

PKG=multigit
python3 setup.py --quiet sdist
sudo -H pip3 install --quiet --upgrade dist/*
