from typing import List


console_scripts: List[str] = [
    "pymultigit=pymultigit.main:main",
]
config_requires: List[str] = []
dev_requires: List[str] = [
    "pypitools",
]
make_requires: List[str] = [
    "pyclassifiers",
    "pymakehelper",
    "pydmt",
]
install_requires: List[str] = [
    "gitpython",
    "pyfakeuse",
    "pytconf",
    "pylogconf",
    "venv-run",
]
test_requires: List[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "flake8",
    "mypy",
]
requires = config_requires + install_requires + make_requires + test_requires
