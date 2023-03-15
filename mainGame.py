from tkinter import *
from tkinter import messagebox
import os


def helpMessages():
    messagebox.showinfo('help', "Use ↑↓←→ to control your snake, eat as much as you can!\np:pause\nb:boss  Don't worry!"
                                " you game will be saved when you press boss key!\ns:save\nYou can enter 'reduce' to"
                                " cheat! ")


def mainGame():
    os.system('python3 getName.py')


def checkHistory():
    os.system('python3 check.py')


def doContinue():
    file = open("continue.txt")
    tx = file.read().rstrip()
    if tx != "0":
        os.system('python3 version2.py')
    else:
        messagebox.showinfo('information', "No previous game")


win = Tk()  # 窗口
win.title("Snake Game")
w = 550
h = 550
ws = win.winfo_screenwidth()  # computers screen size
hs = win.winfo_screenheight()
x = (ws / 2) - (w / 2)  # calculate center
y = (hs / 2) - (h / 2)
win.geometry('%dx%d+%d+%d' % (w, h, x, y))
photo = PhotoImage(file='贪吃蛇.png')
label = Label(win,image = photo,compound='center').pack()

gameflag = False
menu = Menu(win)  # 创建主菜单
menu_main2 = Menu(menu)  # 创建主菜单2
menu_main21 = Menu(menu_main2)  # 创建主菜单21
menu_main21.add_command(label='new', command=lambda: mainGame())  # 子菜单
menu_main21.add_command(label='continue', command=lambda: doContinue())  # 子菜单
menu_main2.add_cascade(label='start', menu=menu_main21)
menu_main2.add_command(label='help', command=lambda: helpMessages())  # 子菜单
menu_main2.add_command(label='check history', command=lambda: checkHistory())  # 子菜单
menu.add_cascade(label='menu', menu=menu_main2)  # 添加主菜单2到主菜单上
win.config(menu=menu)  # 设置主菜单到界面

win.mainloop()
