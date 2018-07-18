from core.lib import loader as load

from tkinter import *
from core.lib import compile_project
import os


file_ment = StringVar()


exists = False


def files(project_name, root):
    global _global_project_name 
    _global_project_name = project_name
    import json

    with open('projects/projects.json') as f:
        data = json.load(f)

    project_details = data['projects'][project_name]
    markdown_paths = project_details['sections']

    def get_markdown_paths(markdown_paths):
        for markdown_path in markdown_paths:
            if '*' in markdown_path:
                markdown_path = markdown_path.split('*')[0]
                files = os.listdir('projects/'+project_name+'/content/'+markdown_path)
                files = sorted(files)

                for file in files:
                    paths.append(markdown_path[:-1]+'/'+file[:-3])
            
            else:
                paths.append(markdown_path)

    paths = []
    get_markdown_paths(markdown_paths)

    global files_frame
    files_frame = Frame()
    files_frame.pack(side=BOTTOM)

    space = Label(files_frame, text='').pack()

    title = Label(files_frame, text=project_name.title(), font='Helvetica 18 bold').pack()

    for path in paths:
        file = Button(files_frame, text=path, command=lambda path=path: project(path, project_name)).pack()

    # create new file
    title = Label(files_frame, text='Create new file:').pack()

    file_name_input = Entry(files_frame, textvariable=file_ment).pack()

    button_create = Button(files_frame, text='Create!', command=gui_create_file).pack(side=LEFT)


def project(path, project_name):
    # edit file
    edit_file_frame = Frame()
    edit_file_frame.pack(side=BOTTOM)

    space = Label(edit_file_frame, text='').pack()

    title = Label(edit_file_frame, text=project_name.title()+': '+path, font='Helvetica 18 bold').pack()

    markdown = load.raw('projects/'+project_name+'/content/'+path+'.md')

    ment = StringVar()
    ment.set(markdown)
    textarea = Text(edit_file_frame, height=20)  # textvariable = ment,
    textarea.insert(END, markdown)
    textarea.pack()


def gui_create_file():
    print(file_ment)
    file_name = file_ment.get().replace(' ', '_')
    file_name = file_name.replace('.', '_')
    
    if len(file_name) > 0 and len(file_name) < 50 and '/' not in file_name:
        file_name = 'projects/'+_global_project_name+'/content/'+file_name+'.md'
        file = open(file_name, "w+")
        print(file_name+' created!')  # add try/catch
        # !! add file to json
        file.close()
    else:
        print('Invalid project name characters or length')