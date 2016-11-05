import click # for group
import os # for chdir, getcwd
import os.path # for dirname
import subprocess # for check_call
import glob # for glob
import sys # for exit

def projects():
    '''
    the method returns tuples of (project_name, project_dir)
    '''
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

@click.group()
@click.option('--verbose/--no-verbose', default=False, is_flag=True)
@click.option('--stats/--no-stats', default=False, is_flag=True)
@click.pass_context
def cli(ctx, verbose, stats):
    ctx.obj=Obj()
    ctx.obj.verbose=verbose
    ctx.obj.stats=stats

@cli.command()
@click.pass_obj
def build(obj):
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
    orig_dir=os.getcwd()
    count=0
    for (project_name, project_dir) in projects():
        count+=1
        os.chdir(project_dir)
        (res_out, res_err, returncode)=run([
            'git',
            'status',
            '--short',
        ])
        if res_out!='' or res_err!='':
            print('project [{0}] is dirty'.format(project_name))
            if obj.verbose:
                print(res_out, end='')
        os.chdir(orig_dir)
    if obj.stats:
        print('scanned [{0}] projects'.format(count))

@cli.command()
@click.pass_obj
def list(obj):
    count=0
    for (project_name, project_dir) in projects():
        count+=1
        if obj.verbose:
            print(project_name, project_dir)
        else:
            print(project_name)
    if obj.stats:
        print('scanned [{0}] projects'.format(count))
