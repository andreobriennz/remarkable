'''
Create Tk instance
Call functions to create frames
Start mainloop
'''


from tkinter import *
import imp


def index():
    root = Tk()

    create_project = imp.load_source('create', 'core/views/create_project.py')
    root = view_create_project.index(root)

    projects = imp.load_source('create', 'core/views/projects.py')
    root = projects.view_projects(root)
    
    root.mainloop()