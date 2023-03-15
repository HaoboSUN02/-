import tkinter
from tkinter import *
file = open("history.txt")
data = file.readlines()
file.close()
data_list = []
for line in data:
    if line == "\n":
        continue
    line = line.rstrip()
    position = line.find(":")
    data_list.append((int(line[position+1:]), line[0:position]))
data_list.sort(reverse=True)
window = tkinter.Tk()
window.title(" top 5 players")
w = 550
h = 550
ws = window.winfo_screenwidth()  # computers screen size
hs = window.winfo_screenheight()
x = (ws / 2) - (w / 2)  # calculate center
y = (hs / 2) - (h / 2)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))
L1 = Label(window, font="Times 20 italic bold", text="%d %s:%s\n%d %s:%s\n%d %s:%s\n%d %s:%s\n%d %s:%s" % (1,data_list[0][1], data_list[0][0], 2,data_list[1][1],data_list[1][0],3,data_list[2][1],data_list[2][0],4,data_list[3][1],data_list[3][0],5,data_list[4][1],data_list[4][0]))

L1.pack(anchor=N, side=LEFT)

window.mainloop()
