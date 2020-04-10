from graphics import *
from math import sqrt

def main():
    win = GraphWin("Triangle Information", 320, 240)
    a = win.getMouse()
    b = win.getMouse()
    c = win.getMouse()
    triangle = Polygon(Point(a.getX(),a.getY()),Point(b.getX(),b.getY()),Point(c.getX(),c.getY())).draw(win)
    side1 = sqrt((b.getY()-a.getY())**2 + (b.getX()-a.getX()))
    side2 = sqrt((c.getY()-b.getY())**2 + (c.getX()-b.getX()))
    side3 = sqrt((a.getY()-c.getY())**2 + (a.getX()-c.getX()))
    perimeter = side1 + side2 + side3
    s = perimeter / 2
    area = sqrt(s*(s-side1)*(s-side2)*(s-side3))
    Text(Point(50,230),"Perimeter: " + str(round(perimeter,2))).draw(win)
    Text(Point(200,230), "Area: " + str(round(area,2))).draw(win)
    win.getMouse()
    
main()