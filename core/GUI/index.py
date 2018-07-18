from tkinter import *
# import imp
# projects = imp.load_source('manage', '../../manage.py')


# should be in core/lib/ and called both here and in manage.py
import imp
import shutil
import json
# projects = imp.load_source('projects', 'core/lib/compile.py')
# create = imp.load_source('create', 'core/lib/create.py')



root = Tk()

gui_create = imp.load_source('create', 'core/GUI/create_project.py')
root = gui_create.index(root)

gui_projects = imp.load_source('create', 'core/GUI/projects.py')
root = gui_projects.index(root)

root.mainloop()


def close(frame):
    pass
