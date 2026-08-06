import tkinter
from tkinter import *

def miles_to_km():
     score_miles = float(input_entry_miles.get())
     score_km = score_miles * 1.609
     my_label_4.config(text=score_km)

window = tkinter.Tk()
window.title('Mile to Km Converter')
window.minsize(width=400, height=300)
window.config(padx=100, pady=100)

my_label_1 = tkinter.Label(text='miles')
my_label_1.grid(row=0, column=2)

my_label_2 = tkinter.Label(text='is equal to')
my_label_2.grid(row=1, column=0)

my_label_4 = tkinter.Label(text=0)
my_label_4.grid(row=1, column=1)

my_label_5 = tkinter.Label(text='km')
my_label_5.grid(row=1, column=2)

input_entry_miles = Entry(width=10)
input_entry_miles.grid(row=0, column=1)

button = Button(text='Calculate', command=miles_to_km)
button.grid(row=2, column=1)
