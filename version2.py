from tkinter import Tk, Canvas, messagebox
import random
import re
import os



def placeFood():
    global food, foodX, foodY
    food = canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="steelblue")
    foodX = random.randint(0, width - snakeSize)
    foodY = random.randint(0, height - snakeSize)
    canvas.move(food, foodX, foodY)


def loadFood(a, b):
    global food, foodX, foodY
    food = canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="steelblue")
    foodX = a
    foodY = b
    canvas.move(food, foodX, foodY)


def leftKey(event):
    global direction
    direction = "left"


def rightKey(event):
    global direction
    direction = "right"


def upKey(event):
    global direction
    direction = "up"


def downKey(event):
    global direction
    direction = "down"


def cheatKey(event):
    if len(snake) > 1:
        deleted = snake.pop()
        coo = canvas.coords(deleted)
        canvas.create_rectangle(coo[0], coo[1], coo[2], coo[3], fill="black")
        positions.pop()


def stopKey(event):
    global stopflag
    stopflag = True
    global foodX, foodY, userName, score, direction
    file = open("continue.txt", "w")
    # 名字和得分
    file.write("%s:%d\n" % (userName, score))
    # 蛇的位置
    for squs in snake:
        file.write(str(canvas.coords(squs)) + "\n")
    # 食物位置
    strFoodX = str(foodX)
    strFoodY = str(foodY)
    file.write(strFoodX + "\n")
    file.write(strFoodY + "\n")
    file.write(direction)
    file.close()
    messagebox.showinfo('pausing', "click ok to continue")
    os.system('python3 version2.py')
    os.system(exit())


def saveKey(event):
    global foodX, foodY, userName, score, direction, stopflag
    stopflag = True
    file = open("continue.txt", "w")
    # 名字和得分
    file.write("%s:%d\n" % (userName, score))
    # 蛇的位置
    for squs in snake:
        file.write(str(canvas.coords(squs))+"\n")
    # 食物位置
    strFoodX = str(foodX)
    strFoodY = str(foodY)
    file.write(strFoodX+"\n")
    file.write(strFoodY+"\n")
    file.write(direction)
    file.close()
    messagebox.showinfo('information', "The game is saved")
    os.system('python3 version2.py')
    os.system(exit())


def bossKey(event):
    global foodX, foodY, userName, score, direction
    file = open("continue.txt", "w")
    # 名字和得分
    file.write("%s:%d\n" % (userName, score))
    # 蛇的位置
    for squs in snake:
        file.write(str(canvas.coords(squs)) + "\n")
    # 食物位置
    strFoodX = str(foodX)
    strFoodY = str(foodY)
    file.write(strFoodX + "\n")
    file.write(strFoodY + "\n")
    file.write(direction)
    file.close()
    os.system('python3 boss.py')
    os.system(exit())


def setWindowDimensions(w, h):
    window = Tk()
    window.title("Snake Game")
    ws = window.winfo_screenwidth()  # computers screen size
    hs = window.winfo_screenheight()
    x = (ws / 2) - (w / 2)  # calculate center
    y = (hs / 2) - (h / 2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    return window


# 牵连对象
def moveFood():
    global food, foodX, foodY
    canvas.move(food, (foodX * (-1)), (foodY * (-1)))
    foodX = random.randint(0, width - snakeSize)
    foodY = random.randint(0, height - snakeSize)
    canvas.move(food, foodX, foodY)


def overlapping(a, b):
    if a[0] < b[2] and a[2] > b[0] and a[1] < b[3] and a[3] > b[1]:
        return True
    return False


# 牵连对象
def moveSnake():
    global positions
    canvas.pack()
    positions = []
    positions.append(canvas.coords(snake[0]))
    if positions[0][0] < 0:
        canvas.coords(snake[0], width, positions[0][1], width - snakeSize, positions[0][3])
    elif positions[0][2] > width:
        canvas.coords(snake[0], 0 - snakeSize, positions[0][1], 0, positions[0][3])
    elif positions[0][3] > height:
        canvas.coords(snake[0], positions[0][0], 0 - snakeSize, positions[0][2], 0)
    elif positions[0][1] < 0:
        canvas.coords(snake[0], positions[0][0], height, positions[0][2], height - snakeSize)
    positions.clear()
    positions.append(canvas.coords(snake[0]))
    if direction == "left":
        canvas.move(snake[0], -snakeSize, 0)
    elif direction == "right":
        canvas.move(snake[0], snakeSize, 0)
    elif direction == "up":
        canvas.move(snake[0], 0, -snakeSize)
    elif direction == "down":
        canvas.move(snake[0], 0, snakeSize)
    sHeadPos = canvas.coords(snake[0])
    foodPos = canvas.coords(food)
    if overlapping(sHeadPos, foodPos):
        moveFood()
        growSnake()
    for i in range(1, len(snake)):
        if overlapping(sHeadPos, canvas.coords(snake[i])):
            gameOver = True
            canvas.create_text(width / 2, height / 2, fill="white", font="Times 20 italic bold", text="Game Over!")
            history = open("history.txt", "a")
            history.write("\n%s:%d" % (userName, score))
            history.close()
            file = open("continue.txt", "w")
            file.write("0")
            file.close()

    for i in range(1, len(snake)):
        positions.append(canvas.coords(snake[i]))
    for i in range(len(snake) - 1):
        canvas.coords(snake[i + 1], positions[i][0], positions[i][1], positions[i][2], positions[i][3])
    if 'gameOver' not in locals():
        if not stopflag:
            window.after(90, moveSnake)


def growSnake():
    lastElement = len(snake) - 1
    lastElementPos = canvas.coords(snake[lastElement])
    snake.append(canvas.create_rectangle(0, 0, snakeSize, snakeSize, fill="#FDF3F3"))
    if direction == "left":
        canvas.coords(snake[lastElement + 1], lastElementPos[0] + snakeSize, lastElementPos[1], lastElementPos[2] + snakeSize, lastElementPos[3])
    elif direction == "right":
        canvas.coords(snake[lastElement + 1], lastElementPos[0] -snakeSize, lastElementPos[1], lastElementPos[2] - snakeSize, lastElementPos[3])
    elif direction == "up":
        canvas.coords(snake[lastElement + 1], lastElementPos[0], lastElementPos[1] + snakeSize, lastElementPos[2], lastElementPos[3] + snakeSize)
    else:
        canvas.coords(snake[lastElement + 1], lastElementPos[0], lastElementPos[1] - snakeSize, lastElementPos[2],lastElementPos[3] - snakeSize)
    global score
    score += 10
    txt = userName + "   score:" + str(score)
    canvas.itemconfigure(scoreText, text=txt)


positions = []
file = open("continue.txt")
datas = file.readlines()
total_lines = len(datas)
data0 = datas[0].rstrip()
positon = data0.find(":")
name = data0[0:positon]
score = int(data0[positon+1:])
file.close()
snake = []
food_x = int(datas[total_lines-3].rstrip())
food_y = int(datas[total_lines-2].rstrip())



userName = name
width = 550
height = 550
window = setWindowDimensions(width, height)
canvas = Canvas(window, bg="black", width=width, height=height)
for i in range(1, total_lines-3):
    data1 = datas[i].rstrip()
    r = '[+,/:@[\\]]+'
    data1 = re.sub(r, '', data1)
    data1 = data1.split()
    a = float(data1[0])
    b = float(data1[1])
    c = float(data1[2])
    d = float(data1[3])
    snake.append(canvas.create_rectangle(a, b, c, d, fill="white"))

stopflag = False
snakeSize = 15
speed = 90
txt = userName + "   Score:" + str(score)
scoreText = canvas.create_text(width / 2, 10, fill="white", font="Times 20 italic bold", text=txt)
canvas.bind("<Left>", leftKey)
canvas.bind("<Right>", rightKey)
canvas.bind("<Up>", upKey)
canvas.bind("<Down>", downKey)
canvas.bind("<r><e><d><u><c><e>", cheatKey)
canvas.bind("<p>", stopKey)
canvas.bind("<s>", saveKey)
canvas.bind("<b>", bossKey)
canvas.focus_set()
direction = datas[total_lines-1].rstrip()
stopValue = False
loadFood(food_x, food_y)
moveSnake()
window.mainloop()
