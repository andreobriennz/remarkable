'''
Create frames and elements
Handle create project on click
'''


from core.lib.crud import create
from core.lib.styles import typography as fonts

from tkinter import *
import shutil
import json


def handle_create_project():
    create.project(ment.get())


def view_create_project(root):
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
    print('Closed create')