"""
main
"""

import sys
from pytconf import register_endpoint
from pytconf import register_main, config_arg_parse_and_launch
import pylogconf.core


from pymultigit.configs import ConfigDebug, ConfigGrep, ConfigMain, ConfigOutput
from pymultigit.core import do_count, is_dirty, has_untracked_files, non_synchronized_with_upstream, \
    do_for_all_projects, do_clean, do_diff, do_status, do_dirty, do_pull, do_grep, do_branch_local, \
    do_branch_remote, print_projects_that_return_data, do_branch_github, do_check_workflow_exists_for_makefile, \
    do_build_bootstrap, do_build_pydmt, do_build_make, do_build_venv_make, do_build_venv_pydmt, \
    do_build_pydmt_build_venv

from pymultigit.static import DESCRIPTION, APP_NAME, VERSION_STR


@register_endpoint(
    configs=[ConfigDebug],
    description="Show the status of multiple git repositories",
)
def count_dirty() -> None:
    do_count(
        is_dirty,
        'is dirty',
        'is clean',
        'were dirty',
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
        'has untracked files',
        'is fully tracked',
        'have untracked files',
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
        'is behind upstream',
        'is synchronized',
        'are behind upstream',
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
    description="run pydmt build on repos",
)
def build_pydmt() -> None:
    do_for_all_projects(do_build_pydmt)


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
        ConfigMain,
        ConfigOutput,
    ],
    description="create pydmt virtual env",
)
def build_pydmt_build_venv() -> None:
    do_for_all_projects(do_build_pydmt_build_venv)


@register_endpoint(
    configs=[
        ConfigDebug,
        ConfigMain,
        ConfigOutput,
    ],
    description="run pydmt build on repos, inside venv",
)
def build_venv_pydmt() -> None:
    do_for_all_projects(do_build_venv_pydmt)


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


if __name__ == '__main__':
    main()
