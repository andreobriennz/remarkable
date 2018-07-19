'''
Open project text area
Close previous text area if exists
On click, save content from project text area
'''


def save_edits():
    markdown = textarea.get("1.0","end-1c")
    
    if len(markdown) > 0:
        save.save(markdown, 'projects/'+global_project_name+'/content/'+global_path+'.md')
        print('saved: '+'projects/'+global_project_name+'/content/'+global_path+'.md')

        _compile.index(global_project_name)
        return

    print('Too short')


def project(path, project_name):
    close()
    
    global global_path
    global_path = path
    global global_project_name
    global_project_name = project_name
    global edit_file_frame
    edit_file_frame = Frame()
    edit_file_frame.pack(side=BOTTOM)

    space = Label(edit_file_frame, text='').pack()

    title = Label(edit_file_frame, text=project_name.title()+': '+path, font=fonts.h2).pack()

    markdown = load.raw('projects/'+project_name+'/content/'+path+'.md')

    global textarea
    textarea = Text(edit_file_frame, height=20)  # textvariable = ment,
    textarea.insert(END, markdown)
    textarea.pack()

    button_save_edit = Button(edit_file_frame, text='Save changes', command=lambda: save_edits()).pack(side=BOTTOM)


def close():
    try:
        edit_file_frame.pack_forget()
        edit_file_frame.destroy()
        print('closed project edit')
    except NameError:
        print('nothing to close')