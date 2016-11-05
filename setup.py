import setuptools

'''
TODO: generate this file automagically
from template.
'''

setuptools.setup(
    name='multigit',
    version='0.0.5',
    description='multigit is a command to help you deal with multiple git repositories',
    long_description='this is the long description of multigit',
    url='https://veltzer.github.io/multigit',
    author='Mark Veltzer',
    author_email='mark.veltzer@gmail.com',
    license='GPL3',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='git python repositories multiple',
    package_dir={'':'src'},
    packages=setuptools.find_packages('src'),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'mg=multigit.mg:cli',
        ],
    },
)
