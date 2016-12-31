#!/usr/bin/python3

import subprocess
import os

module = os.path.basename(os.getcwd())
subprocess.call([
    'gnome-open',
    'https://pythonhosted.org/{module}'.format(module=module),
])
subprocess.call([
    'gnome-open',
    'http://{module}.readthedocs.io/en/latest/'.format(module=module),
])
