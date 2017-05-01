#!/usr/bin/python3

import subprocess
import os

project_name = os.path.basename(os.getcwd())
subprocess.call([
    'gnome-open',
    'https://pythonhosted.org/{project_name}'.format(project_name=project_name),
])
subprocess.call([
    'gnome-open',
    'http://{project_name}.readthedocs.io/en/latest/'.format(project_name=project_name),
])
