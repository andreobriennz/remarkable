from core.lib import create
from core.lib import compile_project
from core.GUI import index as gui

import argparse


version = '0.0.0'


# run with: runp manage.py test
def test(test_string=''):
    if test_string != '':
        print('Test passed! Message: '+test_string)
    else:
        print('Test passed!')
    

def run(project_name):
    compile_project.index(project_name)
    print('Compiled!')


def start_gui():
    gui.index()


# argparse
parser = argparse.ArgumentParser()
parser.add_argument('task')

args = parser.parse_args()

if args.task:
    if args.task == 'version':
        print('Version: '+version)

    elif args.task == 'gui' or args.task == 'open' or args.task == 'start':
        start_gui()
    
    elif 'compile=' in args.task:
        run(args.task.split('compile=')[1])
    
    elif 'create=' in args.task:
        create.create(args.task.split('create=')[1])
