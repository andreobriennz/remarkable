from tkinter import *
# import imp
# projects = imp.load_source('manage', '../../manage.py')


# should be in core/lib/ and called both here and in manage.py
import imp
import shutil
import json
projects = imp.load_source('projects', 'core/lib/compile.py')
def create( project_name ):
    shutil.copytree('core/default_project', 'projects/'+project_name)

    new_project_data = {
        "name": project_name,
        "theme": "",
        "title": "",
        "subtitle": "",
        "sections": ["*"],
    }

    with open('projects/projects.json', 'r+') as f:
        data = json.load(f)
        data['projects'][project_name] = new_project_data
        f.seek(0)        # <--- should reset file position to the beginning.
        json.dump(data, f, indent = 4)
        f.truncate()     # remove remaining part

    print('Created in: projects/'+project_name+'!')


def gui_create_project():
    project_name = ment.get().replace(' ', '_')
    
    if len( project_name ) > 0 and len( project_name ) < 50 and '/' not in project_name:
        create( project_name )
    else:
        print('Invalid project name characters or length')

    


root = Tk()

top_frame = Frame( root )
top_frame.pack()

bottom_frame = Frame( root )
bottom_frame.pack( side = BOTTOM )

title = Label( top_frame, text = 'Create a new project').pack()
description = Label( top_frame, text = 'Enter project name:').pack()

ment = StringVar()
project_name_input = Entry( bottom_frame, textvariable = ment ).pack()

button_create = Button( bottom_frame, text = 'Create!', command = gui_create_project ).pack( side = LEFT )

# List existing projects:
# current_projects_frame = Frame( root )
# current_projects_frame.pack( side = BOTTOM )

# projects_list = Label( top_frame, text = projects_list).pack()


root.mainloop()



# # alt way to consider calling function:
# def gui_create_project_onclick( event ):
#     create( 'test1' )
# button_create.bind( '<Button-1>', gui_create_project ) 
# # '<Button-1>' is *left* click event. '<Button-2>' is *middle* click event. '<Button-3>' is *right* click event.
# button_create.pack( side = LEFT )