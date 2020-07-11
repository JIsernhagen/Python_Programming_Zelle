from graphics import *
from random import *
from math import *


def main():
    x = 0
    y = 0
    n = eval(input("Please input number of steps: "))
    win = GraphWin("Random Walk in Two Dimensions", 100, 100)
    win.setCoords(-50, -50.0, 50, 50)
    Circle(Point(0, 0), 2).draw(win)
    for i in range(n):
        xold = x
        yold = y
        angle = random() * 2 * pi
        x += cos(angle)
        y += sin(angle)
        Line(Point(xold,yold), Point(x, y)).draw(win)

    print("Final position after " + str(n) + " steps is (" + str(x) + ", " + str(y) + ").")
    x = win.getMouse()

def step():
    step = random()
    if step <= 0.25:
        return 0, 1
    elif step <= .5:
        return 1, 0
    elif step <= .75:
        return -1, 0
    else:
        return 0, -1

main()