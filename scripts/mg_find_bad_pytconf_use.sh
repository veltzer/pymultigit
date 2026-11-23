#!/bin/bash -eu
{ pymultigit grep --regexp "from pytconf.config import" || true; } | grep -v pytconf/pytconf
