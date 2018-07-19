import shutil
import json


def project(project_name):
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


def ensurePathsExist(paths):
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)