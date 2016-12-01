'''
dependencies for this project
'''

def populate(d):
    d.requirements3_dev=[
        #'sphinx-pypi-upload',
    ]
    d.requirements3=[
        'click',
        'gitpython',
    ]

def getdeps():
    return [
        __file__, # myself
    ]
