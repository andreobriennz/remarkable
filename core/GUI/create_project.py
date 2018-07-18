from core.lib import create

from tkinter import *
import shutil
import json


def gui_create_project():
    project_name = ment.get().replace(' ', '_')
    
    if len(project_name) > 0 and len(project_name) < 50 and '/' not in project_name:
        print(project_name)
        create.create(project_name)
        # Tk.update()
    else:
        print('Invalid project name characters or length')


def index(root):
    global top_frame
    global bottom_frame

    top_frame = Frame(root)
    top_frame.pack()

    bottom_frame = Frame(root)
    bottom_frame.pack()

    title = Label(top_frame, text='Create a new project', font='Helvetica 18 bold').pack()
    description = Label(top_frame, text='Enter project name:').pack()

    global ment
    ment = StringVar()
    project_name_input = Entry(bottom_frame, textvariable=ment).pack()

    button_create = Button(bottom_frame, text = 'Create!', command = gui_create_project).pack( side = LEFT )

    return root

# # alt way to consider calling function:
# def gui_create_project_onclick( event ):
#     create( 'test1' )
# button_create.bind( '<Button-1>', gui_create_project ) 
# # '<Button-1>' is *left* click event. '<Button-2>' is *middle* click event. '<Button-3>' is *right* click event.
# button_create.pack( side = LEFT )


def close():
    top_frame.pack_forget()
    bottom_frame.pack_forget()
    top_frame.destroy()
    bottom_frame.destroy()
    print('closed top create')