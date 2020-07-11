from graphics import *
from math import sqrt

def target_draw(win):
    center = Point(0,0)
    circle1 = Circle(center, 50)
    circle1.setFill("white")
    circle2 = Circle(center, 40)
    circle2.setFill("black")
    circle3 = Circle(center, 30)
    circle3.setFill("blue")
    circle4 = Circle(center, 20)
    circle4.setFill("red")
    circle5 = Circle(center, 10)
    circle5.setFill("yellow")
    circle1.draw(win)
    circle2.draw(win)
    circle3.draw(win)
    circle4.draw(win)
    circle5.draw(win)

def main():
    win = GraphWin("Archery Target", 320, 320)
    win.setCoords(-100, -100, 100, 100)
    target_draw(win)
    score = 0
    for i in range(5):
        p = win.getMouse()
        arrow = Point(p.getX(), p.getY())
        radius = sqrt(p.getX()**2 + p.getY()**2)
        print("radius " + str(i) + ": " + str(radius))
        if radius <=10:
            score+=9
        elif radius <=20:
            score+=7
        elif radius <=30:
            score+=5
        elif radius <=20:
            score+=3
        elif radius <=10:
            score+=1
    print("Score: " + str(score))
    p = win.getMouse()
    win.close()

main()