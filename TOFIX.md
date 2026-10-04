# TOFIX

Findings from a code scan on 2026-10-04.

## High

- `src/pymultigit/core.py:128` - `non_synchronized_with_upstream` is a stub that always returns `False`, so the `synchronized` command (`src/pymultigit/main.py:105`) reports every repo as synchronized regardless of state. Implement it (e.g. `git rev-list --left-only --count @...@{upstream}`, as `do_status` already does on lines 272-278) or remove the command.
- `src/pymultigit/core.py:234` - `do_branch_github` returns the branch name, but `branch_github` runs it through `do_for_all_projects` (`src/pymultigit/main.py:98`), which discards return values; the command prints nothing but the project names. Print the value (or use `print_projects_that_return_data`).
- `src/pymultigit/core.py:226` - `git branch --remotes --show-current` ignores `--remotes` and prints the local branch (verified: prints `master`), so `branch_remote` is just a duplicate of `branch_local`. Use `git rev-parse --abbrev-ref @{upstream}` to show the tracked remote branch.

## Medium

- `src/pymultigit/core.py:181-182` - `do_check_workflow_exists_for_makefile` returns a bool, but `print_projects_that_return_data` prints every project whose result `is not None` (line 109), so all projects are listed and `True`/`False` is printed as their data. Return `None` for the "ok" case and a message otherwise.
- `src/pymultigit/core.py:209` - `pipe.returncode` is read inside the `with Popen(...)` block before the process is waited on, so it is always `None` and git grep failures are never raised; `stderr=subprocess.PIPE` (line 202) is also never drained, which can block git on large error output. Call `pipe.wait()` before checking, and handle git grep's exit code 1 (no match) separately from real errors.
- `src/pymultigit/configs.py:57-60` - `ConfigMain.glob` (default `*/*.git`) is exposed as a CLI option but never read; `projects()` hardcodes `*/.git` and `*/**/.git` (`src/pymultigit/core.py:28-30`). Use the option or remove it.
- `src/pymultigit/main.py:180-189` - `pull` does not register `ConfigPull`, and `build_venv_make` (line 168) does not register `ConfigSubprocess`, so `--pull_quiet`, `--print_command` and `--quiet` read by `do_pull` (`core.py:176`) and `check_call_ve` (`utils/subprocess.py:25-27`) can never be set from the command line. Add the configs to the endpoints.
- `src/pymultigit/core.py:153` - `build_venv_make` only acts on repos with `.venv/default`; no repo under ~/git has that layout any more (repos use `.venv`), so the command is a silent no-op fleet-wide. Update to `.venv` or remove it together with `utils/subprocess.py` and the `venv-run` dependency.
- `pyproject.toml:37` - `pyfakeuse` is a declared runtime dependency but nothing under src/, tests/ or scripts/ imports it. Remove it.
- `scripts/mg_check_same_files.sh:12` - the helper scripts still target the pre-migration fleet layout: `.veltzer.tag` markers, `templates/*.mako` (lines 63-73), `config/project.py` (`scripts/mg_find_no_license.sh:2`), `config/python.py` (`scripts/mg_find_redundant_sphinx.sh:6`), `requirements.thawed.txt` (`scripts/mg_all_upgrade_deps.sh:6`), `templates/...build.yml.mako` (`scripts/mg_dont_have_flow_template.sh:7`) and `MANIFEST.in` (`scripts/mg_find_no_manifest.sh:4`); none of these exist in any repo under ~/git now, so the scripts report nothing useful or fail. Delete them (rsmultigit check-same covers the same-file checks) or port the ones still wanted.
- `scripts/mg_find_suggest_config.sh:2` - calls `mr`, which is not installed; port to `pymultigit grep` like `scripts/mg_grep_noinspection.sh` or delete.

## Low

- `src/pymultigit/core.py:288-289` - `--git_quiet` makes `do_dirty` run `git status --porcelain --quiet`, and `git status` has no `--quiet` option (exits 129). Do not add `--quiet` for `git status`.
- `scripts/mg_branch_not_master.sh:17` - prints `${branch}` (the local branch) in the "remote" message, and `git branch -r -q --show-current` on line 14 returns the local branch anyway (same issue as `core.py:226`).
- `pyproject.toml:90` - `mypy_path = "src:python:scripts"` lists a `python` directory that does not exist; drop it.
- `rsconstruct.toml:60` - the sphinx processor's `dep_inputs = ["src/pymultigit/*.py"]` does not cover `src/pymultigit/utils/*.py`, so changes there do not rebuild the docs. Use `src/pymultigit/**/*.py`.
- `src/pymultigit/configs.py:88` - the help string for `ConfigGrep.files` is a copy of the one for `regexp` ("what regexp to look for?"); describe it as the pathspec to limit the grep to.
- `doc/TODO.txt:5` - lists already-implemented items: the `diff` command (`main.py:219-224`), the "no projects found" message (`core.py:116-117`) and stop-on-failure (`ConfigMain.stop`, `configs.py:69-72`). Prune them.
