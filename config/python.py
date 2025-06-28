""" python deps for this project """

console_scripts: list[str] = [
    "pymultigit=pymultigit.main:main",
]

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
    "pytest-cov",
    "mypy",
]
requires = config_requires + install_requires + build_requires + test_requires
