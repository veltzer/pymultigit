#!/bin/bash -eu
pymultigit grep --regexp "from pytconf.config import" | grep -v pytconf/pytconf
