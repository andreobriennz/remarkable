from tkinter import *
import os
import imp
# import shutil
projects = imp.load_source('projects', 'core/lib/compile.py')


def files(project_name, root):
    # view files frame
    #  adapted from lib/compile.py. Move into own folder or lib/load.py
    import json
    load = imp.load_source('loader', 'core/lib/loader.py')

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

    files_frame = Frame()
    files_frame.pack(side = BOTTOM)

    space = Label(files_frame, text = '').pack()

    title = Label(files_frame, text = project_name.title(), font='Helvetica 18 bold').pack()

    for path in paths:
        file = Button(files_frame, text = path, command = lambda path = path: project(path, project_name)).pack()



def project(path, project_name):
    # edit file
    edit_file_frame = Frame()
    edit_file_frame.pack(side = BOTTOM)

    space = Label(edit_file_frame, text = '').pack()

    title = Label(edit_file_frame, text = project_name.title()+': '+path, font='Helvetica 18 bold').pack()

    load = imp.load_source('loader', 'core/lib/loader.py')
    markdown = load.raw( 'projects/'+project_name+'/content/'+path+'.md' )

    ment = StringVar()
    ment.set(markdown)
    textarea = Text(edit_file_frame, height=20)  # textvariable = ment,
    textarea.insert(END, markdown)
    textarea.pack()
    
    # loop and output projects
    # projects = os.listdir('projects')
    # projects = sorted(projects)