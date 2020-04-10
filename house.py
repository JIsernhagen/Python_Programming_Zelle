from graphics import *

def main():
    win = GraphWin("Five-click House", 320, 240)
    a = win.getMouse()
    b = win.getMouse()
    base = Rectangle(Point(a.getX(),a.getY()),Point(b.getX(),b.getY())).draw(win)

    c = win.getMouse()
    doorhalfwidth = abs(a.getX()-b.getX()) / 10
    door = Rectangle(Point(c.getX()-doorhalfwidth,c.getY()),Point(c.getX()+doorhalfwidth,a.getY())).draw(win)

    d = win.getMouse()
    window = Rectangle(Point(d.getX()-doorhalfwidth, d.getY()-doorhalfwidth), Point(d.getX()+doorhalfwidth, d.getY()+doorhalfwidth)).draw(win)

    e = win.getMouse()
    Line(Point(e.getX(),e.getY()),Point(a.getX(),b.getY())).draw(win)
    Line(Point(e.getX(),e.getY()),Point(b.getX(),b.getY())).draw(win)

    win.getMouse()

main()