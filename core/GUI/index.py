from tkinter import *
import imp

def quit(self):
    print('close')
    self.root.destroy()

def index():
    root = Tk()

    gui_create = imp.load_source('create', 'core/GUI/create_project.py')
    root = gui_create.index(root)

    gui_projects = imp.load_source('create', 'core/GUI/projects.py')
    root = gui_projects.index(root)
    
    root.mainloop()