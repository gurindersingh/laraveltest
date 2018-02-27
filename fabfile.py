from __future__ import with_statement
from fabric.api import cd, run, env
from fabric.decorators import task

env.use_ssh_config = True
env.hosts = ['lp-app']

@task
def deploy():
    with cd('/home/lpdeployer/laravelplus.com/current/repo'):
        run('git pull origin master')
        run('composer install')