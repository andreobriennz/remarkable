from tkinter import *
import imp
projects = imp.load_source('projects', 'core/lib/compile.py')
create = imp.load_source('create', 'core/lib/create.py')


def gui_create_project():
    project_name=ment.get().replace(' ', '_')
    
    if len(project_name) > 0 and len(project_name) < 50 and '/' not in project_name:
        create.create(project_name)
    else:
        print('Invalid project name characters or length')


def index(root):
    top_frame = Frame(root)
    top_frame.pack()

    bottom_frame = Frame(root)
    bottom_frame.pack()

    title = Label(top_frame, text='Create a new project', font='Helvetica 18 bold').pack()
    description = Label(top_frame, text='Enter project name:').pack()

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