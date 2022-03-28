from tkinter import *
from tkinter import ttk
from tkinter import messagebox


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

master = Tk()

variable = StringVar(master)
variable.set(OPTIONS[0])

w = OptionMenu(master, variable, *OPTIONS)
w.pack()

thisdict = {
    "New York": "5176810",
    "Washington D.C.": "1527390",
    "Hiroshima": "1021990",
    "Moscow": "5122060",
    "Kviv": "1725180",
    "Berlin": "2157280",
    "London": "3794140",
    "Beijing": "4880650",
    "New Delhi": "9081680",
    "San Francisco": "1113760",
    "Rio de Janeiro": "3591720",
    "Baghdad": "5171790",
    "Islamabad": "2112580"
}

def ok():
    print ("Country: " + variable.get() + " Casualty Count:" + (thisdict[variable.get()]) )

button = Button(master, text="OK", command=ok)
button.pack()



mainloop()