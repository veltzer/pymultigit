'''
dependencies for this project
'''

def populate(d):
    d.requirements3_dev=[
        #'sphinx-pypi-upload',
        'click',
    ]

def getdeps():
    return [
        __file__, # myself
    ]
