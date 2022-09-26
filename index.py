from math import fabs
from turtle import *
from random import choice, random

redBg = False
redBgBt = False

bricksBottom = int(input("Enter the number of bricks in the bottom layer: ") or 5) 
if bricksBottom < 1 and bricksBottom > 25:
    print("Invalid number of bricks provided in the bottom layer.")
    exit()

bricksTop = int(input("Enter the number of bricks in the top layer: ") or 1) 
if bricksTop < 1:
    print("Invalid number of bricks provided in the top layer.")
    exit()

if bricksTop > bricksBottom:
    print("Number of bricks in the top layer cannot be greater than the number of bricks in the bottom layer.")
    exit()

brickWidth = int(input("Enter the width of each brick: ") or 30) 
if brickWidth < 1 and brickWidth > 35:
    print("Invalid width of each brick provided.")
    exit()

brickHeight = int(input("Enter the height of each brick: ") or 20) 
if brickHeight < 1 and brickHeight > 25:
    print("Invalid height of each brick provided.")
    exit()

wn = Screen()
wn.bgcolor("lightgreen")
wn.title("Bricks")
wn.screensize(canvheight=500,canvwidth=300)
b = Turtle()

numberoflayers = (bricksBottom - bricksTop + 1)

b.speed(0)



print(screensize())

def drawbricks( width, height):
        b.begin_fill()
        for j in range(2):
            b.forward(width)
            b.left(90)
            b.forward(height)
            b.left(90)
        b.end_fill()
        b.penup()
        b.forward(width)
        b.pendown()


for i in range(numberoflayers):
    if i == 0 or i==numberoflayers-1:
        redBgBt = True
    else:
        redBgBt = False
    b.penup()
    b.goto(((0+i*brickWidth)/2), 0 + i * brickHeight)
    b.pendown()
    for j in range(bricksBottom-i):
        if j == 0 or j == bricksBottom-(i+1):
            redBg = True
        else:
            redBg = False

        if redBg or redBgBt:
            randomcolor = "red"
        else:
            randomcolor = '#' + ''.join([choice('0123456789ABCDEF') for k in range(6)])
        b.fillcolor(randomcolor)
        drawbricks(brickWidth, brickHeight)

done()
