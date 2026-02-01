# Digital clock

import tkinter as tk
from time import strftime

root = tk.Tk()
root.title("Digital Clock")

def time():
    string = strftime('%H:%M:%S %p \n %d/%m/%Y')
    label.config(text=string)
    label.after(1000, time)

label = tk.Label(root, font=('Arial Rounded MT Bold', 60, 'bold'), background='yellow', foreground='black')
label.pack(anchor='center')

time()

root.mainloop()