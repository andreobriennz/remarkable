from tkinter import *
# import imp
# projects = imp.load_source('manage', '../../manage.py')


import imp


root = Tk()

gui_create = imp.load_source('create', 'core/GUI/create_project.py')
root = gui_create.index(root)

gui_projects = imp.load_source('create', 'core/GUI/projects.py')
root = gui_projects.index(root)

root.mainloop()


# add function to close frames
# def close(frame):
#     pass
