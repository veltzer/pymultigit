""" python depedencies for this project """
from typing import List


console_scripts: List[str] = [
    "pymultigit=pymultigit.main:main",
]
dev_requires: List[str] = [
    "pypitools",
]
config_requires: List[str] = [
    "pyclassifiers",
]
install_requires: List[str] = [
    "gitpython",
    "pyfakeuse",
    "pytconf",
    "pylogconf",
    "venv-run",
]
build_requires: List[str] = [
    "pymakehelper",
    "pydmt",
]
test_requires: List[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "flake8",
    "mypy",
]
requires = config_requires + install_requires + build_requires + test_requires
