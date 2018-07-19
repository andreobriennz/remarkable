'''
Open project files list
Handle selecting file
Handle creating file
'''


from core.lib import load
from core.lib import save
from core.lib import _compile
from core.views.lib import typography as fonts

from tkinter import *
import os


file_ment = StringVar()


def files(project_name, root):
    global _global_project_name 
    _global_project_name = project_name
    import json

    with open('projects/projects.json') as f:
        data = json.load(f)

    project_details = data['projects'][project_name]
    markdown_paths = project_details['sections']

    def get_markdown_paths(markdown_paths):
        for markdown_path in markdown_paths:
            if '*' in markdown_path:
                markdown_path = markdown_path.split('*')[0]
                files = os.listdir('projects/'+project_name+'/content/'+markdown_path)
                files = sorted(files)

                for file in files:
                    paths.append(markdown_path[:-1]+'/'+file[:-3])
            
            else:
                paths.append(markdown_path)

    paths = []
    get_markdown_paths(markdown_paths)

    global files_frame
    files_frame = Frame()
    files_frame.pack(side=BOTTOM)

    space = Label(files_frame, text='').pack()

    title = Label(files_frame, text=project_name.title(), font=fonts.h2).pack()

    for path in paths:
        file = Button(files_frame, text=path, command=lambda path=path: project(path, project_name)).pack()

    # create new file
    title = Label(files_frame, text='Create new file:').pack()

    file_name_input = Entry(files_frame, textvariable=file_ment).pack()

    button_create = Button(files_frame, text='Create!', command=gui_create_file).pack(side=LEFT)


def gui_create_file():
    print(file_ment)
    global file_frame
    file_name = file_ment.get().replace(' ', '_')
    file_name = file_name.replace('.', '_')
    
    if len(file_name) > 0 and len(file_name) < 50 and '/' not in file_name:
        file_name = 'projects/'+_global_project_name+'/content/'+file_name+'.md'
        file = open(file_name, "w+")
        print(file_name+' created!')  # add try/catch
        # !! add file to json
        file.close()
    else:
        print('Invalid project name characters or length')