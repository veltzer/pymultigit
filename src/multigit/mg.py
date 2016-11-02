import click # for group
import os # for chdir, getcwd
import os.path # for dirname
import subprocess # for check_call
import glob # for glob

def dirs_of_repos():
    for x in glob.glob('*/.git'):
        yield os.path.dirname(x)

@click.group()
def cli():
    pass

@cli.command()
def build():
    orig_dir=os.getcwd()
    for dir in dirs_of_repos():
        os.chdir(dir)
        subprocess.check_call([
            'git',
            'status',
            '--short',
        ])
    os.chdir(orig_dir)

@cli.command()
def status():
    orig_dir=os.getcwd()
    for dir in dirs_of_repos():
        os.chdir(dir)
        subprocess.check_call([
            'git',
            'status',
            '--short',
        ])
    os.chdir(orig_dir)

@cli.command()
def list():
    for dir in dirs_of_repos():
        print(dir)
