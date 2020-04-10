from graphics import *

def main():
    win = GraphWin("Face", 320, 240)
    center = Point(160, 120)
    outline = Circle(center, 80)
    eyeleft = Circle(Point(120, 90), 10)
    eyeright = Circle(Point(200, 90), 10)
    nose = Circle(center, 15)
    mouth = Oval(Point(110, 150), Point(210, 170))
    outline.draw(win)
    eyeleft.draw(win)
    eyeright.draw(win)
    nose.draw(win)
    mouth.draw(win)
    p = win.getMouse()

main()