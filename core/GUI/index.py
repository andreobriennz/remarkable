from tkinter import *

root = Tk() # root = blank window

label = Label(root, text = 'Hello, world!') # to make text, output to root, 

label.pack() # most simple/quick way to position it (just dumps label most obvious place)

root.mainloop() # tells root to put this infinate loop, rather than outputting it and then disapearing 

