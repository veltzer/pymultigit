import click
import os
import os.path
import subprocess
import glob
import sys
import git

def projects():
    """
    the method returns tuples of (project_name, project_dir)
    """
    repos_list=glob.glob('*/.git')
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
def status(obj):
    """ show the status of multiple git repositories """
    count=0
    count_dirty=0
    for (project_name, project_dir) in projects():
        count+=1
        repo = git.Repo(project_dir)
        dirty = repo.is_dirty()
        if dirty:
            count_dirty+=1
        if obj.verbose:
            if dirty:
                print('project [{}] is dirty'.format(project_name))
            else:
                print('project [{}] is clean'.format(project_name))
    if obj.stats:
        print('scanned [{0}] projects'.format(count))
        print('[{0}] projects were dirty'.format(count_dirty))

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
