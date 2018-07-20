'''
Create frames and elements
Handle create project on click
'''


from core.lib import create
from core.views.lib import typography as fonts

from tkinter import *
import shutil
import json


def gui_create_project():
    project_name = ment.get().replace(' ', '_')
    
    if len(project_name) > 0 and len(project_name) < 50 and '/' not in project_name:
        print(project_name)
        create.create(project_name)
    else:
        print('Invalid project name characters or length')


def index(root):
    global top_frame
    global bottom_frame

    top_frame = Frame(root)
    top_frame.pack()

    bottom_frame = Frame(root)
    bottom_frame.pack()

    title = Label(top_frame, text='Create a new project', font=fonts.h2).pack()
    description = Label(top_frame, text='Enter project name:').pack()

    global ment
    ment = StringVar()
    project_name_input = Entry(bottom_frame, textvariable=ment).pack()

    button_create = Button(bottom_frame, text = 'Create!', command = handle_create_project).pack( side = LEFT )

    return root


def close():
    top_frame.pack_forget()
    bottom_frame.pack_forget()
    top_frame.destroy()
    bottom_frame.destroy()
    print('closed top create')