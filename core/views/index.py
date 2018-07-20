'''
Create Tk instance
Call functions to create frames
Start mainloop
'''


from tkinter import *
import imp


def index():
    root = Tk()

    create_project = imp.load_source('create_project', 'core/views/create_project.py')
    root = create_project.view_create_project(root)

    projects = imp.load_source('projects', 'core/views/projects.py')
    root = projects.view_projects(root)
    
    root.mainloop()