from graphics import *
from math import sqrt

def main():
    win = GraphWin("Line segment information", 320,240)
    a = win.getMouse()
    b = win.getMouse()
    line = Line(Point(a.getX(),a.getY()),Point(b.getX(),b.getY())).draw(win)
    midpoint = Point((a.getX()+ b.getX())/2, (a.getY()+ b.getY())/2)
    midpoint.setFill("cyan")
    midpoint.draw(win)
    length = sqrt(((a.getX()+ b.getX())/2)**2 + ((a.getY()+ b.getY())/2)**2)
    rise = b.getY()-a.getY()
    run = b.getX()-a.getX()
    if run !=0:
        slope = str(round(rise / run,2))
    else:
        slope = "Slope is undefined."
    Text(Point(50,230),"Length: " + str(round(length,2))).draw(win)
    Text(Point(200,230),"Slope: " + slope).draw(win)
    win.getMouse()

main()