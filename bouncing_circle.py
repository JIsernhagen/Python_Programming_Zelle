from graphics import *
from time import sleep

def main():
    win = GraphWin("Bouncing Ball", 480, 480)
    win.setCoords(-100, -100, 100, 100)
    p = win.getMouse()
    center = Point(p.getX(), p.getY())
    dx = 1
    dy = 1
    ball = Circle(center, 3)
    ball.draw(win)
    for i in range(10000):
        p = ball.getCenter()
        x = p.getX()
        y = p.getY()
        print(center.getX())
        print(center.getY())
        if x >= 100:
            dx = -1
        if x <= -100:
            dx = 1
        if y >= 100:
            dy = -1
        if y <= -100:
            dy = 1
        ball.move(dx,dy)
        sleep(0.005)


    p = win.getMouse()
    win.close()

main()