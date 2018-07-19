'''
Create Tk instance
Call functions to create frames
Start mainloop
'''


from tkinter import *
import imp


def index():
    root = Tk()

    gui_create = imp.load_source('create', 'core/views/create_project.py')
    root = gui_create.index(root)

    gui_projects = imp.load_source('create', 'core/views/projects.py')
    root = gui_projects.index(root)
    
    root.mainloop()