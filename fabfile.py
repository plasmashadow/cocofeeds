from fabric.api import local


def transform():
    local('python `which coconut` .')

def run_server():
    local('python main.py')

def dev(watch=True):
    transform()
    run_server()
