# not currently used - but CLI and GUI should both call this to keep code DRY
import imp
import shutil
import json
projects = imp.load_source('projects', 'core/lib/compile.py')


def create(project_name):
    shutil.copytree('core/default_project', 'projects/'+project_name)

    new_project_data = {
        "name": project_name,
        "theme": "",
        "title": "",
        "subtitle": "",
        "sections": ["*"],
    }

    with open('projects/projects.json', 'r+') as f:
        data = json.load(f)
        data['projects'][project_name] = new_project_data
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent=4)
        f.truncate()     # remove remaining part

    print('Created in: projects/'+project_name+'!')
