import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("Snake Game")
w = 700
h = 700
ws = window.winfo_screenwidth()  # computers screen size
hs = window.winfo_screenheight()
x = (ws / 2) - (w / 2)  # calculate center
y = (hs / 2) - (h / 2)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))
photo = PhotoImage(file='boss1.png')
label = Label(window, image=photo, compound='center').pack()
window.mainloop()
