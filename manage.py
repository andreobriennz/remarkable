import imp
projects = imp.load_source('projects', 'core/lib/compile.py')

import shutil

version = '0.0.0'

# run with: runp manage.py test
def test( test_string = '' ):
    if test_string != '':
        print('Test passed! Message: '+test_string)
    else:
        print('Test passed!')
    

def run( project_name ):
    projects.index( project_name)
    print('Compiled!')

def create( project_name ):
    shutil.copytree('core/default_project', 'projects/'+project_name)
    print('Created in: projects/'+project_name+'!')