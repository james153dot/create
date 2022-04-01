from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import Tk
import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD, Font
from tkinter.ttk import Label


root = tk.Tk()
root.title('Warning')

label = ttk.Label(
    root,
    text='Close This Tab To View the Casulties of Nuclear War',
    font=("Helvetica", 30))

label.pack(ipadx=10, ipady=10)

root.mainloop()


root = Tk()



OPTIONS = [
"New York",
"Washington D.C.",
"Hiroshima",
"Moscow",
"Kviv",
"Berlin",
"London",
"Beijing",
"New Delhi",
"San Francisco",
"Rio de Janeiro",
"Baghdad",
"Islamabad"
]

variable = StringVar(root)
variable.set(OPTIONS[0])

w = OptionMenu(root, variable, *OPTIONS)
w.pack()

thisdict = {
    "New York": 5176810,
    "Washington D.C.": 1527390,
    "Hiroshima": 1021990,
    "Moscow": 5122060,
    "Kviv": 1725180,
    "Berlin": 2157280,
    "London": 3794140,
    "Beijing": 4880650,
    "New Delhi": 9081680,
    "San Francisco": 1113760,
    "Rio de Janeiro": 3591720,
    "Baghdad": 5171790,
    "Islamabad": 2112580
}

def printtext():
    global deads
    int = deads.get() 
    print (int)   

class text(Frame):
    def __init__(self, parent, text):
        super().__init__(parent)
        self.label = Label(self, text=text, anchor="s")
        self.label.pack(side="left", fill="both", expand=True)

def by_value(item):
    return item[1]

def dead():
    print ("City: " + str(variable.get()) + " will have an approximate casualty count of " + str((thisdict[variable.get()])) + " people")
    count = len(root.winfo_children())
    item = text(root, "There will be " + str((thisdict[variable.get()])) + " dead in " + str(variable.get()))
    item.pack(side="top", fill="x")

deads = Entry(root, font=('calibre',10,'normal'))
deads.pack()
deads.focus_set()

b = Button(root,text='okay',command=printtext)
b.pack(side='bottom')

def max():
    for k, v in sorted(thisdict.items(), key=by_value):
        if v > int(deads.get()):
            item = text(root, "Cities with more than " + deads.get() + " dead are " + k)
            item.pack(side="top", fill="x")

button1 = Button(root, text = "Cities with Maximum Dead", command = max, font=('calibre',15, 'bold'))
button2 = Button(root, text = "Amount Dead", command=dead)
button1.pack()
button2.pack()

root.geometry("1000x600")

mainloop()