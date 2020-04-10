from graphics import *

def main():
    win = GraphWin("Rectangle Information", 320, 240)
    a = win.getMouse()
    b = win.getMouse()
    rectangle = Rectangle(Point(a.getX(),a.getY()),Point(b.getX(),b.getY())).draw(win)

    area = abs(b.getX()-a.getX()) * abs(b.getY()-a.getY())
    perimeter = 2 * abs(b.getX()-a.getX()) + 2 * abs(b.getY()-b.getY())

    Text(Point(50,230),"Area: "+ str(round(area, 2))).draw(win)
    Text(Point(200,230),"Perimeter: "+ str(round(perimeter))).draw(win)

    win.getMouse()

main()
