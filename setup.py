import setuptools

'''
TODO: generate this file automagically
from template.
'''

setuptools.setup(
    name='pymultigit',
    version='0.0.12',
    description='pymultigit is a command to help you deal with pymultiple git repositories',
    long_description='this is the long description of pymultigit',
    url='https://veltzer.github.io/pymultigit',
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
        'gitpython',
    ],
    entry_points={
        'console_scripts': [
            'mg=pymultigit.mg:cli',
        ],
    },
)
