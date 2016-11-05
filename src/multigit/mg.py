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

@click.group(short_help="short help")
@click.option('--verbose/--no-verbose', default=False, is_flag=True, help='help for verbose')
@click.option('--stats/--no-stats', default=False, is_flag=True, help='help for stats')
@click.pass_context
def cli(ctx, verbose, stats):
    """ doc for cli """
    ctx.obj=Obj()
    ctx.obj.verbose=verbose
    ctx.obj.stats=stats

@cli.command()
@click.pass_obj
def build(obj):
    ''' doc for build '''
    orig_dir=os.getcwd()
    for (project_name, project_dir) in projects():
        os.chdir(project_dir)
        (res_out, res_err, returncode)=run([
            'git',
            'status',
            '--short',
        ])
        os.chdir(orig_dir)

@cli.command(help="this is help")
@click.pass_obj
def status(obj):
    """
    doc for status
    """
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
    ''' doc for list '''
    count=0
    for (project_name, project_dir) in projects():
        count+=1
        if obj.verbose:
            print(project_name, project_dir)
        else:
            print(project_name)
    if obj.stats:
        print('scanned [{0}] projects'.format(count))

if __name__=='__main__':
    cli()
