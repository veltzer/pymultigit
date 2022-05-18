import config.project

package_name = config.project.name

console_scripts = [
    "pymultigit=pymultigit.main:main",
]
dev_requires = [
    "pyclassifiers",
    "pypitools",
    "pydmt",
    "Sphinx",
]
install_requires = [
    "gitpython",
    "pyfakeuse",
    "pytconf",
    "pylogconf",
    "venv-run",
]
test_requires = [
    "pylint",
    "pytest",
    "pytest-cov",
    "flake8",
    "pymakehelper",
]

python_requires = ">=3.10"

test_os = ["ubuntu-22.04"]
test_python = ["3.10"]
