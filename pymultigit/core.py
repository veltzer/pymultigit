import glob
import os
import os.path
import subprocess
import sys

import git
from pyfakeuse.pyfakeuse import fake_use

from pymultigit.configs import ConfigAll


def projects(sort: bool):
    """
    the method returns tuples of (project_name, project_dir)
    """
    repos_list = glob.glob('*/.git')
    if sort:
        repos_list.sort()
    if len(repos_list) == 0:
        print('no git repos here', file=sys.stderr)
        sys.exit(1)
    for x in repos_list:
        yield os.path.dirname(x), os.path.dirname(x)


def run(args, do_exit=True):
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (res_out, res_err) = p.communicate()
    res_out = res_out.decode()
    res_err = res_err.decode()
    if p.returncode:
        print('errors while running [{0}]...'.format(args))
        print(res_out, end='', file=sys.stderr)
        print(res_err, end='', file=sys.stderr)
        if do_exit:
            sys.exit(p.returncode)
    return res_out, res_err, p.returncode


def do_count(fnc, attr_name, not_attr_name, attr_plural):
    count = 0
    count_attr = 0
    for (project_name, project_dir) in projects(sort=ConfigAll.sort):
        count += 1
        repo = git.Repo(project_dir)
        attr = fnc(repo)
        if attr:
            count_attr += 1
        if ConfigAll.verbose:
            if attr:
                print('project [{project_name}] {attr_name}'.format(
                    project_name=project_name,
                    attr_name=attr_name,
                ))
            else:
                print('project [{project_name}] {not_attr_name}'.format(
                    project_name=project_name,
                    not_attr_name=not_attr_name,
                ))
    if ConfigAll.stats:
        print('scanned [{count}] projects'.format(
            count=count,
        ))
        print('[{count_attr}] projects {attr_plural}'.format(
            count_attr=count_attr,
            attr_plural=attr_plural,
        ))


def do_for_all_projects(fnc):
    count = 0
    count_not_found = 0
    count_error = 0
    count_ok = 0
    orig_dir = os.getcwd()
    for (project_name, project_dir) in projects(sort=ConfigAll.sort):
        if ConfigAll.verbose:
            print('doing [{0}] at [{1}]...'.format(project_name, project_dir), end='')
            sys.stdout.flush()
        count += 1
        if os.path.isdir(project_dir):
            os.chdir(project_dir)
            ret = fnc(project_name, project_dir)
            if ret:
                count_error += 1
            else:
                count_ok += 1
            if ConfigAll.verbose:
                print('OK')
            os.chdir(orig_dir)
        else:
            if ConfigAll.verbose:
                print('NOT FOUND')
            count_not_found += 1
    if ConfigAll.stats:
        print('scanned [{}] projects'.format(count))
        print('[{}] not found'.format(count_not_found))
        print('[{}] error'.format(count_error))
        print('[{}] ok'.format(count_ok))


def is_dirty(repo):
    return repo.is_dirty()


def has_untracked_files(repo):
    return len(repo.untracked_files) > 0


def non_synchronized_with_upstream(repo):
    fake_use(repo)
    return False


def do_build(project_name: str, project_dir: str):
    fake_use(project_name)
    makefile = os.path.join(project_dir, 'Makefile')
    bootstrap = os.path.join(project_dir, 'bootstrap')
    if os.path.isfile(makefile):
        pass
    if os.path.isfile(bootstrap):
        pass
    if ConfigAll.stats:
        pass


def do_pull(project_name: str, project_dir: str):
    fake_use(project_name, project_dir)
    args = ['git', 'pull']
    if ConfigAll.verbose:
        args.append('--verbose')
    if ConfigAll.quiet:
        args.append('--quiet')
    return subprocess.call(args)


def do_grep(project_name: str, project_dir: str):
    fake_use(project_name, project_dir)
    args = ['git', 'grep', ConfigAll.regexp]
    if ConfigAll.verbose:
        args.append('--verbose')
    if ConfigAll.quiet:
        args.append('--quiet')
    return subprocess.call(args)


def do_clean(project_name: str, project_dir: str):
    fake_use(project_name, project_dir)
    args = ['git', 'clean', '-ffxd']
    if ConfigAll.quiet:
        args.append('--quiet')
    return subprocess.call(args)


def do_status_msg(project_name: str, msg: str):
    (res_out, res_err, return_code) = run([
        'git',
        'status',
        # porcelain is guaranteed to have parsable output and not
        # change across git versions
        '--porcelain',
        # when using --porcelain branch information is not shown,
        # this flag makes it not so, the problem with it is that
        # it produces output which should be parsed and that is
        # why we do not used it and use the 'git rev-list' that follows...
        # '--branch'
        # '--short',
    ])
    if res_out != '' or res_err != '':
        print(msg.format(project_name=project_name))
        if ConfigAll.verbose:
            print(res_out, end='')
            print(res_err, end='')
        return 1
    (res_out, res_err, return_code) = run([
        'git',
        'rev-list',
        '--left-only',
        '--count',
        '@...@{upstream}',
    ])
    if res_out != '0\n' or res_err != '':
        print('project [{0}] is not synced'.format(project_name))
        if ConfigAll.verbose:
            print(res_out, end='')
            print(res_err, end='')
        return 1
    return 0


def do_status(project_name: str, project_dir: str):
    fake_use(project_dir)
    return do_status_msg(project_name=project_name, msg='project [{project_name}] is dirty')


def do_dirty(project_name: str, project_dir: str):
    fake_use(project_dir)
    return do_status_msg(project_name=project_name, msg='{project_name}')


def do_print(project_name: str, project_dir: str):
    if ConfigAll.verbose:
        print(project_name, project_dir)
    else:
        print(project_name)
    return 0


