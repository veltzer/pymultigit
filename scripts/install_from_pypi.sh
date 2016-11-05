#!/bin/sh

PKG=multigit
sudo -H pip3 install --quiet --upgrade $PKG
pip3 show $PKG | grep -e "^Version"
