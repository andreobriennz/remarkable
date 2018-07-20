import os
import shutil
import json


def project(project_name):
    project_name = project_name.replace(' ', '_')
    
    if len(project_name) == 0 or len(project_name) > 50 or '/' in project_name:
        print('Invalid project name characters or length')
        return

    shutil.copytree('core/lib/default_project', 'projects/'+project_name)

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


def file(file_path, file_name):
    file_name = file_name.replace(' ', '_')

    if len(file_name) < 2 or len(file_name) > 50 or '/' in file_name:
        print('Invalid project name characters or length')
        return

    file_name = file_path+file_name
    file = open(file_name, "w+")
    file.close()
    print(file_name+' created!')


def ensurePathsExist(paths):
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)