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
    'venv-run',
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

python_requires = ">=3.7"

extras_require = {
}

# https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners
test_os = "[ubuntu-18.04, ubuntu-20.04]"
test_python = "[3.7, 3.8, 3.9]"
test_container = "[ 'ubuntu:18.04', 'ubuntu:20.04' ]"
