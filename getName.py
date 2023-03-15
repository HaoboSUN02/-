import tkinter
from tkinter import *
import os


def reg():
    file = open("store.txt", "w")
    file.write(e_user.get())
    file.close()
    os.system('python3 version1.py')




if __name__ == "__main__":
    window = tkinter.Tk()
    window.title("Snake Game")
    w = 550
    h = 550
    ws = window.winfo_screenwidth()  # computers screen size
    hs = window.winfo_screenheight()
    x = (ws / 2) - (w / 2)  # calculate center
    y = (hs / 2) - (h / 2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    l_user = Label(window, text='Please enter your name：')
    l_user.grid(row=0, sticky=W)
    e_user = Entry(window)
    e_user.grid(row=0, column=1, sticky=E)

    b_login = Button(window, text='start', command=reg)
    b_login.grid(row=2, column=1, sticky=E)
    window.mainloop()
