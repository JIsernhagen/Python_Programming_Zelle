from graphics import *

def main():
    mouseclicks = []
    xsum = 0
    ysum = 0
    xysum = 0
    xsquaredsum = 0
    n = 0
    win = GraphWin("Regression Line", 320, 240)
    Rectangle(Point(0,0),Point(50,30)).draw(win)
    win.setCoords(0.0, 0.0, 320.0, 240.0)
    Text(Point(25, 15), "Chart").draw(win)
    while True:
        p = win.getMouse()
        if (p.getX() < 50 and p.getY() < 30): break
        Circle(p, 2).draw(win)
        print("You clicked at:" + str(p.getX()) + "," + str(p.getY()))
        xsum+=p.getX()
        ysum+=p.getY()
        xysum+=p.getX() * p.getY()
        xsquaredsum+=(p.getX()**2)
        n+=1
        mouseclicks.append(p)
    print("Loop exited")
    xmean = xsum/n
    ymean = ysum/n
    m = (xysum - (n*xmean*ymean)) / (xsquaredsum - n * xmean**2)
    yleft = (ysum/n) + m*(0-xmean)
    yright = (ysum/n) + m*(320-xmean)
    Line(Point(0,yleft),Point(320,yright)).draw(win)

    print(mouseclicks)
    x = win.getMouse()

main()
