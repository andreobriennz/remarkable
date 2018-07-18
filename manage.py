import imp
import shutil
import json
import argparse

projects = imp.load_source('projects', 'core/lib/compile.py')
create = imp.load_source('create', 'core/lib/create.py')

version = '0.0.0'

# run with: runp manage.py test
def test(test_string = ''):
    if test_string != '':
        print('Test passed! Message: '+test_string)
    else:
        print('Test passed!')
    

def run(project_name):
    projects.index( project_name)
    print('Compiled!')


def start_gui():
    gui_create_project = imp.load_source('gui_create_project', 'core/GUI/index.py')


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
