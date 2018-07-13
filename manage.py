import imp
import shutil
import json
projects = imp.load_source('projects', 'core/lib/compile.py')

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

    new_project_data = {
        "name": project_name,
        "theme": "",
        "title": "",
        "subtitle": "",
        "sections": [],
    }

    with open('projects/projects.json', 'r+') as f:
        data = json.load(f)
        data['projects'][project_name] = new_project_data
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent = 4)
        f.truncate()     # remove remaining part

    print('Created in: projects/'+project_name+'!')


def start_gui():
    gui_create_project = imp.load_source('gui_create_project', 'core/GUI/create_project.py')