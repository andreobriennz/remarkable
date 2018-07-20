from tkinter import Text, Entry, Label


def TextArea(frame, text, height, width, font, style):
    textarea = Text(frame, height=height, width=width, font=font)
    textarea.insert(END, text)

    return textarea


def Input(frame, ment):
    entry = Entry(frame, textvariable=ment)

    return entry


def Text(frame, text, font, style):
    text = Label(top_frame, text=text, font=font)

    return text


def Br(frame):
    br = Label(frame, text='')


# IDs = []


# def Div(name, root):
#     div = Frame(root)

#     IDs[name] = {
#         'name': name,
#         'type': 'frame',
#         'frame': div,
#         'active': None,
#     }