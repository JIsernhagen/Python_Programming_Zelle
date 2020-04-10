from graphics import *

def main():
    win = GraphWin("Winter Scene", 320, 240)
    floor = Rectangle(Point(0, 230), Point(320,240))
    floor.setFill("white")
    snow1 = Circle(Point(80, 190), 40)
    snow1.setFill("white")
    snow2 = Circle(Point(80, 120), 30)
    snow2.setFill("white")
    eyeleft = Circle(Point(70,110), 2)
    eyeleft.setFill("black")
    eyeright = Circle(Point(90,110), 2)
    eyeright.setFill("black")
    nose = Circle(Point(80, 120), 3)
    nose.setFill("orange")
    mouth1 = Circle(Point(65,123), 2)
    mouth1.setFill("black")
    mouth2 = Circle(Point(73,129), 2)
    mouth2.setFill("black")
    mouth3 = Circle(Point(80,130), 2)
    mouth3.setFill("black")
    mouth4 = Circle(Point(89,129), 2)
    mouth4.setFill("black")
    mouth5 = Circle(Point(95,123), 2)
    mouth5.setFill("black")
    treebase = Rectangle(Point(200, 220), Point(220, 230))
    treebase.setFill("brown")
    tree = Polygon(Point(180,220), Point(240,220), Point(200,30))
    tree.setFill("green")
    floor.draw(win)
    snow1.draw(win)
    snow2.draw(win)
    eyeleft.draw(win)
    eyeright.draw(win)
    nose.draw(win)
    mouth1.draw(win)
    mouth2.draw(win)
    mouth3.draw(win)
    mouth4.draw(win)
    mouth5.draw(win)
    treebase.draw(win)
    tree.draw(win)


    p = win.getMouse()
3
main()
