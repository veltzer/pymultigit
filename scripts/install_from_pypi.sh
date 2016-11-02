#!/bin/sh

PKG=multigit
sudo -H pip3 install --quiet --upgrade multigit
pip3 show multigit | grep -e "^Version"
