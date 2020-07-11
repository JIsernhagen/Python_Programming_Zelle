from graphics import *
from math import sqrt

def main():
    win = GraphWin("Circle Intersection", 320, 320)
    win.setCoords(-10,-10,10,10)
    y_axis = Line(Point(0,10),Point(0,-10)).draw(win)
    x_axis = Line(Point(-10,0),Point(10,0)).draw(win)
    Text(Point(-8,9),"Radius: ").draw(win)
    rad_input = Entry(Point(-5,9),5).draw(win)
    Text(Point(2,9),"Y-int: ").draw(win)
    int_input = Entry(Point(5,9),5).draw(win)
    win.getMouse()

    #Conversions
    radius = eval(rad_input.getText())
    intercept = eval(int_input.getText())
    circle = Circle(Point(0,0),radius).draw(win)
    line = Line(Point(-10,intercept),Point(10,intercept)).draw(win)
    if radius >= intercept:
        rdot = Point(sqrt(radius**2-intercept**2),intercept)
        rdot.setFill("red")
        rdot.draw(win)
        ldot = Point(-sqrt(radius**2-intercept**2),intercept)
        ldot.setFill("red")
        ldot.draw(win)
        Text(Point(-7,-9),"({0:0.2f},{1})".format(sqrt(radius**2-intercept**2),intercept)).draw(win)
        #Text(Point(-7,-9),"({0:0.2f},{1}), (-{3:0.2f},{4})".format(sqrt(radius**2-intercept**2),intercept,sqrt(radius**2-intercept**2),intercept)).draw(win)
    else:
        Text(Point(-5,-9), "There is no intercept.").draw(win)
    win.getMouse()
    win.close()

main()