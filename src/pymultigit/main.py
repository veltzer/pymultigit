"""
main
"""

import sys

import pylogconf.core
from pytconf import config_arg_parse_and_launch, register_endpoint, register_main

from pymultigit.configs import ConfigDebug, ConfigGrep, ConfigMain, ConfigOutput
from pymultigit.core import (
    do_branch_github,
    do_branch_local,
    do_branch_remote,
    do_build_bootstrap,
    do_build_make,
    do_build_venv_make,
    do_check_workflow_exists_for_makefile,
    do_clean,
    do_count,
    do_diff,
    do_dirty,
    do_for_all_projects,
    do_grep,
    do_pull,
    do_status,
    has_untracked_files,
    is_dirty,
    non_synchronized_with_upstream,
    print_projects_that_return_data,
)
from pymultigit.static import APP_NAME, DESCRIPTION, VERSION_STR


@register_endpoint(
    configs=[ConfigDebug],
    description="Show the status of multiple git repositories",
)
def count_dirty() -> None:
    do_count(
        is_dirty,
        "is dirty",
        "is clean",
        "were dirty",
        True,
        False,
    )


@register_endpoint(
    configs=[ConfigDebug],
    description="Show which repositories have untracked files",
)
def untracked() -> None:
    do_count(
        has_untracked_files,
        "has untracked files",
        "is fully tracked",
        "have untracked files",
        True,
        False,
    )


@register_endpoint(
    configs=[
        ConfigDebug,
        ConfigMain,
        ConfigOutput,
    ],
    description="Show which local branch we are on",
)
def branch_local() -> None:
    do_for_all_projects(do_branch_local)


@register_endpoint(
    configs=[
        ConfigDebug,
        ConfigMain,
        ConfigOutput,
    ],
    description="Show which remote branch we are on",
)
def branch_remote() -> None:
    do_for_all_projects(do_branch_remote)


@register_endpoint(
    configs=[
        ConfigDebug,
        ConfigMain,
        ConfigOutput,
    ],
    description="Show the branch on the github side",
)
def branch_github() -> None:
    do_for_all_projects(do_branch_github)


@register_endpoint(
    configs=[ConfigDebug],
    description="Show which repositories are not synchronized with their upstream",
)
def synchronized() -> None:
    do_count(
        non_synchronized_with_upstream,
        "is behind upstream",
        "is synchronized",
        "are behind upstream",
        True,
        False,
    )


@register_endpoint(
    configs=[
        ConfigDebug,
        ConfigMain,
        ConfigOutput,
    ],
    description="Clean all projects using git removing any files not known to git",
)
def clean_hard() -> None:
    do_for_all_projects(do_clean)


@register_endpoint(
    configs=[ConfigDebug],
    description="Show the status of multiple git repositories",
)
def status() -> None:
    print_projects_that_return_data(do_status)


@register_endpoint(
    configs=[ConfigDebug],
    description="Show names of projects which are dirty",
)
def dirty() -> None:
    print_projects_that_return_data(do_dirty)


@register_endpoint(
    configs=[
        ConfigDebug,
        ConfigMain,
        ConfigOutput,
    ],
    description="run bootstrap build on repos",
)
def build_bootstrap() -> None:
    do_for_all_projects(do_build_bootstrap)


@register_endpoint(
    configs=[
        ConfigDebug,
        ConfigMain,
        ConfigOutput,
    ],
    description="run make build on repos",
)
def build_make() -> None:
    do_for_all_projects(do_build_make)


@register_endpoint(
    configs=[
        ConfigDebug,
        ConfigMain,
        ConfigOutput,
    ],
    description="run make build on repos, inside venv",
)
def build_venv_make() -> None:
    do_for_all_projects(do_build_venv_make)


@register_endpoint(
    configs=[
        ConfigDebug,
        ConfigOutput,
        ConfigMain,
    ],
    description="Pull changes for multiple git repositories",
)
def pull() -> None:
    do_for_all_projects(do_pull)


@register_endpoint(
    description="Check various things",
)
def check_workflow_exists_for_makefile() -> None:
    print_projects_that_return_data(do_check_workflow_exists_for_makefile)


@register_endpoint(
    configs=[
        ConfigDebug,
        ConfigMain,
        ConfigOutput,
        ConfigGrep],
    description="Grep multiple repositories for pattern",
)
def grep() -> None:
    do_for_all_projects(do_grep)


@register_endpoint(
    configs=[ConfigDebug],
    description="List all projects",
)
def list_projects() -> None:
    print_projects_that_return_data(lambda: "")


@register_endpoint(
    configs=[ConfigDebug],
    description="diff all projects",
)
def diff() -> None:
    do_for_all_projects(do_diff)


@register_main(
    main_description=DESCRIPTION,
    app_name=APP_NAME,
    version=VERSION_STR,
)
def main():
    pylogconf.core.setup()
    # make sure stdout is line buffered
    sys.stdout.reconfigure(line_buffering=True)
    config_arg_parse_and_launch()


if __name__ == "__main__":
    main()
