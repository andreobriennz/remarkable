from core.GUI import project

from tkinter import *
import os

import imp


def open_project(project_name, projects_frame, root):
    projects_frame.pack_forget()  # replace with close function in index file
    # projects_frame.destroy()  # if not using again
    project.files(project_name, root)  # consider passing root from index to make more modular

    # close create
    gui_create = imp.load_source('create', 'core/GUI/create_project.py')
    gui_create.close()


def index(root):
    global projects_frame
    projects_frame = Frame(root)
    projects_frame.pack(side=BOTTOM)

    space = Label(projects_frame, text='').pack()

    title = Label(projects_frame, text='Current Projects:', font='Helvetica 18 bold').pack()
    
    # loop and output projects
    projects = os.listdir('projects')
    projects = sorted(projects)
    
    for project in projects:
        if project[:1] != '.' and project[:1] != '_' and '.json' not in project:
            project_title = Button(projects_frame, text=project, command=lambda project=project: open_project(project, projects_frame, root)).pack()
        
    return root
