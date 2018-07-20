'''
Open project text area
Close previous text area if exists
On click, save content from project text area
'''


from core.lib.crud import load
from core.lib.crud import save
from core.lib.crud import _compile
from core.lib.crud import create
from core.views import project_edit
from core.lib.styles import typography as fonts


from tkinter import *


def save_edits():
    markdown = textarea.get("1.0","end-1c")

    if len(markdown) < 1:
        print('Too short to save')
        return
    
    save.save(markdown, 'projects/'+global_project_name+'/content/'+global_path+'.md')

    _compile.compile(global_project_name)


def view_project(path, project_name):
    close()
    
    global global_path
    global global_project_name
    global edit_file_frame
    global textarea

    global_path = path
    global_project_name = project_name

    edit_file_frame = Frame()
    edit_file_frame.pack(side=BOTTOM)

    br = Label(edit_file_frame, text='').pack()

    title = Label(edit_file_frame, text=project_name.title()+': '+path, font=fonts.h2).pack()

    markdown = load.raw('projects/'+project_name+'/content/'+path+'.md')

    textarea = Text(edit_file_frame, height=20)  # textvariable = ment,
    textarea.insert(END, markdown)
    textarea.pack()

    button_save_edit = Button(edit_file_frame, text='Save changes', command=lambda: save_edits()).pack(side=BOTTOM)


def close():
    try:
        edit_file_frame.pack_forget()
        edit_file_frame.destroy()
        print('Closed project edit frame')
    except NameError:
        print('nothing to close')