'''
Open project files list
Handle selecting file
Handle creating file
'''


from core.lib.crud import load
from core.lib.crud import save
from core.lib.crud import _compile
from core.lib.crud import create
from core.views import project_edit
from core.lib.styles import typography as fonts

from tkinter import *
import os
import imp


file_ment = StringVar()


def get_markdown_paths(markdown_paths, project_name):
    paths = []

    for markdown_path in markdown_paths:
        if '*' in markdown_path:
            markdown_path = markdown_path.split('*')[0]
            files = os.listdir('projects/'+project_name+'/content/'+markdown_path)
            files = sorted(files)

            for file in files:
                paths.append(markdown_path[:-1]+'/'+file[:-3])
        
        else:
            paths.append(markdown_path)
    
    return paths


def view_files(project_name, root):
    handle_close_create_project()

    global _global_project_name 
    _global_project_name = project_name
    import json

    with open('projects/projects.json') as f:
        data = json.load(f)

    project_details = data['projects'][project_name]
    markdown_paths = project_details['sections']

    paths = get_markdown_paths(markdown_paths, project_name)

    global files_frame
    files_frame = Frame()
    files_frame.pack(side=BOTTOM)

    space = Label(files_frame, text='').pack()

    title = Label(files_frame, text=project_name.title(), font=fonts.h2).pack()

    for path in paths:
        file = Button(files_frame, text=path, command=lambda path=path: project_edit.view_project(path, project_name)).pack()

    title = Label(files_frame, text='Create new file:').pack()

    file_name_input = Entry(files_frame, textvariable=file_ment).pack()

    button_create = Button(files_frame, text='Create!', command=handle_create_file).pack(side=LEFT)


def handle_create_file():
    file_name = file_ment.get()
    create.file('projects/'+_global_project_name+'/content/', file_name+'.md')


def handle_close_create_project():
    create_project = imp.load_source('create_project', 'core/views/create_project.py')
    create_project.close()