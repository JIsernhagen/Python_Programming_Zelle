from graphics import *

def main():
    win = GraphWin("Square Copier", 320, 240)
    shape = Rectangle(Point(45,45),Point(55,55))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)
    for i in range(3):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        newshape = shape.clone()
        newshape.draw(win)
        newshape.move(dx, dy)
    label = Text(Point(80,10), "Click again to quit")
    label.draw(win)
    p = win.getMouse()
    win.close()

main()



