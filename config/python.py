""" python deps for this project """

scripts: dict[str,str] = {
    "pymultigit": "pymultigit.main:main",
}

config_requires: list[str] = [
    "pyclassifiers",
]
install_requires: list[str] = [
    "gitpython",
    "pyfakeuse",
    "pytconf",
    "pylogconf",
    "venv-run",
]
build_requires: list[str] = [
    "pydmt",
    "pymakehelper",
]
test_requires: list[str] = [
    "pylint",
    "pytest",
    "mypy",
    "ruff",
]
requires = config_requires + install_requires + build_requires + test_requires
