"""
main
"""

from pytconf import register_endpoint
from pytconf import register_main, config_arg_parse_and_launch
import pylogconf.core


from pymultigit.configs import ConfigDebug, ConfigGrep
from pymultigit.core import do_count, is_dirty, has_untracked_files, non_synchronized_with_upstream, \
    do_for_all_projects, do_clean, do_status, do_dirty, do_build, do_pull, do_grep, do_print, do_local_branch, \
    do_remote_branch, print_projects_that_return_true, do_github_branch
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
    configs=[ConfigDebug],
    description="Show which local branch we are on",
)
def local_branch() -> None:
    do_for_all_projects(do_local_branch, True)


@register_endpoint(
    configs=[ConfigDebug],
    description="Show which local branch we are on",
)
def remote_branch() -> None:
    do_for_all_projects(do_remote_branch, True)


@register_endpoint(
    configs=[ConfigDebug],
    description="Show the branch on the github side",
)
def github_branch() -> None:
    do_for_all_projects(do_github_branch, True)


@register_endpoint(
    configs=[ConfigDebug],
    description="Show which repositories are synchronized with their upstream",
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
    configs=[ConfigDebug],
    description="Clean all projects",
)
def clean() -> None:
    do_for_all_projects(do_clean, False)


@register_endpoint(
    configs=[ConfigDebug],
    description="Show the status of multiple git repositories",
)
def status() -> None:
    do_for_all_projects(do_status, False)


@register_endpoint(
    configs=[ConfigDebug],
    description="Show names of project which are dirty",
)
def dirty() -> None:
    print_projects_that_return_true(do_dirty)


@register_endpoint(
    configs=[ConfigDebug],
    description="Build multiple git repositories",
)
def build() -> None:
    do_for_all_projects(do_build, False)


@register_endpoint(
    configs=[ConfigDebug],
    description="Pull changes for multiple git repositories",
)
def pull() -> None:
    do_for_all_projects(do_pull, False)


@register_endpoint(
    configs=[ConfigDebug, ConfigGrep],
    description="Grep multiple repositories for pattern",
)
def grep() -> None:
    do_for_all_projects(do_grep, False)


@register_endpoint(
    configs=[ConfigDebug],
    description="List all projects",
)
def list_projects() -> None:
    do_for_all_projects(do_print, False)


@register_main(
    main_description=DESCRIPTION,
    app_name=APP_NAME,
    version=VERSION_STR,
)
def main():
    pylogconf.core.setup()
    config_arg_parse_and_launch()


if __name__ == '__main__':
    main()
