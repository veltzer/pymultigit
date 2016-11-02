#!/usr/bin/python3

'''
This script registers your project in pypi via setuptools.

It does:
- full clean
- call for registration
- full clean

NOTE!!!
- It seems that registering packages is no longer supported via twine. Just upload the package.
This is the error that I got:
Registering package to https://upload.pypi.org/legacy/
Registering awskit-0.0.1-py2.py3-none-any.whl
HTTPError: 410 Client Error: This API is no longer supported, instead simply upload the file.

So to register you need to:
python setup.py register -r pypi

registering the same package many times works.
You just need to do it once...:)

References:
- https://packaging.python.org/distributing/
'''

import common # for git_clean_full
import subprocess # for check_call, DEVNULL

common.git_clean_full()
subprocess.check_call([
    'python',
    'setup.py',
    'register',
    '-r',
    'pypi',
], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
common.git_clean_full()
