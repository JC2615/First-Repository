
import tkinter as tk


root = tk.Tk()
v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [
    "English",
    "Spanish",
    "French",
    "Russian",
    "Japanese",
]

def ShowChoice():
    print(v.get())

tk.Label(root, 
         text="""Select language:""",
         justify = tk.LEFT,
         padx = 70).pack()
for val, language in enumerate(languages):
    tk.Radiobutton(root, 
                  text=language,
                  padx = 20, 
                  variable=v, 
                  command=ShowChoice,
                  value=val).pack(anchor=tk.W)
    print("initial key: ", val)
    print("initial value: ", language)
root.mainloop()

##############################################################################################

import tkinter
from tkinter import *

root = Tk()
root.title('Random')
Label(text='What would you like translated or defined').pack(side=TOP,padx=10,pady=10)

entry = Entry(root, width=10)
entry.pack(side=TOP,padx=10,pady=10)

def onok():
    x, y = entry.get().split('x')
    for row in range(int(y)):
        for col in range(int(x)):
            print((col, row))

Button(root, text='OK', command=onok).pack(side=LEFT)
Button(root, text='CLOSE').pack(side= RIGHT)
confirm = Button(root, text='Confirm',command = lambda:retrieve_input()).pack()

def retrieve_input(): 
        inputValue = textBox.get("1.0","end-1c")
        print(inputValue)


root.mainloop()
