from graphics import *

def drawFace(center, size, win):
    outline = Circle(center, 80)
    eyeleft = Circle(center, 10)
    eyeleft.move(-30, -30)
    eyeright = Circle(center, 10)
    eyeright.move(30, -30)
    nose = Circle(center, 15)
    mouth = Circle(center, 20)
    mouth.move(0,40)
    outline.draw(win)
    eyeleft.draw(win)
    eyeright.draw(win)
    nose.draw(win)
    mouth.draw(win)


def main():
    sizes = [3, 6, 5, 8]
    centers_x = [160, 130, 80, 220]
    centers_y = [40, 120, 80, 100]
    win = GraphWin("Faces", 320, 240)
    for i, size in enumerate(sizes):
        center = Point(centers_x[i], centers_y[i])
        drawFace(center, size, win)
    p = win.getMouse()

main()