import config.project

package_name = config.project.project_name

console_scripts = [
    'pymultigit=pymultigit.main:main',
]

setup_requires = [
]

run_requires = [
    'gitpython',
    'pyfakeuse',
    'pytconf',
    'pylogconf',
]

test_requires = [
    'pylint',
    'pytest',
    'pytest-cov',
    'flake8',
    'pymakehelper',
]

dev_requires = [
    'pyclassifiers',
    'pypitools',
    'pydmt',
    'Sphinx',
]

install_requires = list(setup_requires)
install_requires.extend(run_requires)

python_requires = ">=3.6"

extras_require = {
}
