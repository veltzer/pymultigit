#!/bin/sh

PKG=multigit
sudo -H pip3 install --quiet --upgrade multigit==0.0.3
pip3 show multigit | grep -e "^Version"
