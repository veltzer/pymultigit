import click
import os
import os.path
import subprocess
import glob
import sys
import git

sort = True

def projects():
    """
    the method returns tuples of (project_name, project_dir)
    """
    repos_list=glob.glob('*/.git')
    if sort:
        repos_list.sort()
    if len(repos_list)==0:
        print('no git repos here', file=sys.stderr)
        sys.exit(1)
    for x in repos_list:
        yield (os.path.dirname(x), os.path.dirname(x))

def run(args, exit=True):
    p=subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (res_out, res_err)=p.communicate()
    res_out=res_out.decode()
    res_err=res_err.decode()
    if p.returncode:
        print('errors while running [{0}]...'.format(args))
        print(res_out, end='', file=sys.stderr)
        print(res_err, end='', file=sys.stderr)
        if exit:
            sys.exit(p.returncode)
    return (res_out, res_err, p.returncode)

class Obj(object):
    pass

def do_count(obj, function, attr_name, not_attr_name, attr_plural):
    count=0
    count_attr=0
    for (project_name, project_dir) in projects():
        count+=1
        repo = git.Repo(project_dir)
        attr = function(repo)
        if attr:
            count_attr+=1
        if obj.verbose:
            if attr:
                print('project [{project_name}] {attr_name}'.format(
                    project_name=project_name,
                    attr_name=attr_name,
                ))
            else:
                print('project [{project_name}] {not_attr_name}'.format(
                    project_name=proejct_name,
                    not_attr_name=not_attr_name,
                ))
    if obj.stats:
        print('scanned [{count}] projects'.format(
            count=count,
        ))
        print('[{count_attr}] projects {attr_plural}'.format(
            count_attr=count_attr,
            attr_plural=attr_plural,
        ))

def is_dirty(repo):
    return repo.is_dirty()

def has_untracked_files(repo):
    return len(repo.untracked_files)>0

def synced_with_upstream(repo):
    return True

@click.group(short_help="short help")
@click.option('--verbose/--no-verbose', default=False, is_flag=True, help='be verbose')
@click.option('--stats/--no-stats', default=False, is_flag=True, help='show statstics at the end')
@click.pass_context
def cli(ctx, verbose, stats):
    """ multigit allows you to perform operations on multiple git repositories """
    ctx.obj=Obj()
    ctx.obj.verbose=verbose
    ctx.obj.stats=stats

@cli.command()
@click.pass_obj
def build(obj):
    """ build multiple git repositories """
    orig_dir=os.getcwd()
    for (project_name, project_dir) in projects():
        os.chdir(project_dir)
        (res_out, res_err, returncode)=run([
            'git',
            'status',
            '--short',
        ])
        os.chdir(orig_dir)

@cli.command()
@click.pass_obj
def dirty(obj):
    """ show the status of multiple git repositories """
    do_count(obj, is_dirty, 'is dirty', 'is clean', 'were dirty')


@cli.command()
@click.pass_obj
def untracked(obj):
    """ show which repositories have untracked files """
    do_count(obj, has_untracked_files, 'has untracked files', 'is fully tracked', 'have untracked files')


@cli.command()
@click.pass_obj
def synched(obj):
    """ show which repositories are synchronized with their upsteam """
    do_count(obj, synced_with_upstream, 'is behind upstream', 'is synched', 'are behind upstream')


@cli.command()
@click.pass_obj
def status_old(obj):
    """ show the status of multiple git repositories """
    orig_dir=os.getcwd()
    count=0
    for (project_name, project_dir) in projects():
        count+=1
        os.chdir(project_dir)
        (res_out, res_err, returncode)=run([
            'git',
            'status',
            # porcelain is guaranteed to have parsable output and not
            # change across git versions
            '--porcelain',
            #'--short',
        ])
        if res_out!='' or res_err!='':
            print('project [{0}] is dirty'.format(project_name))
            if obj.verbose:
                print(res_out, end='')
                print(res_err, end='')
        os.chdir(orig_dir)
    if obj.stats:
        print('scanned [{0}] projects'.format(count))

@cli.command()
@click.pass_obj
def list(obj):
    """ list all projects """
    count=0
    for (project_name, project_dir) in projects():
        count+=1
        if obj.verbose:
            print(project_name, project_dir)
        else:
            print(project_name)
    if obj.stats:
        print('scanned [{0}] projects'.format(count))

@cli.command()
@click.pass_obj
def clean(obj):
    """ clean all projects """
    count=0
    count_not_found=0
    count_error=0
    count_ok=0
    orig_dir=os.getcwd()
    for (project_name, project_dir) in projects():
        if obj.verbose:
            print('cleaning [{0}] at [{1}]...'.format(project_name, project_dir), end='')
            sys.stdout.flush()
        count+=1
        if os.path.isdir(project_dir):
            os.chdir(project_dir)
            ret = subprocess.call(['git','clean','-qffxd'])
            if ret:
                count_error+=1
            else:
                count_ok+=1
            if obj.verbose:
                print('OK')
            os.chdir(orig_dir)
        else:
            if obj.verbose:
                print('NOT FOUND')
            count_not_found+=1
    if obj.stats:
        print('scanned [{}] projects'.format(count))
        print('[{}] not found'.format(count_not_found))
        print('[{}] error'.format(count_error))
        print('[{}] ok'.format(count_ok))


if __name__=='__main__':
    cli()
