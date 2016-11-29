#!/bin/sh
python3 setup.py build_sphinx
#python3 setup.py upload_sphinx -r https://pypi.python.org/pypi
python3 setup.py upload_sphinx
