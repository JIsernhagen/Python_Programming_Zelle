from graphics import *

def main():
    win = GraphWin("Archery Target", 320, 240)
    center = Point(100,100)
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

    p = win.getMouse()
    win.close()
main()