'''
Create frame to view list of projects
Call function to open project on click
Close frame when project open
'''


from core.views import project
from core.views.lib import typography as fonts

from tkinter import *
import os

import imp


def open_project(project_name, root):
    project.files(project_name, root)
    close()


def index(root):
    global projects_frame
    projects_frame = Frame(root)
    projects_frame.pack(side=BOTTOM)

    space = Label(projects_frame, text='').pack()

    title = Label(projects_frame, text='Current Projects:', font=fonts.h2).pack()
    
    # loop and output projects
    projects = os.listdir('projects')
    projects = sorted(projects)
    
    for project in projects:
        if project[:1] != '.' and project[:1] != '_' and '.json' not in project:
            project_title = Button(projects_frame, text=project, command=lambda project=project: open_project(project, root)).pack()
        
    return root


def close():
    projects_frame.pack_forget()
    projects_frame.destroy()
    print('closed project')