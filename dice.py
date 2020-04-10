from graphics import *
def main():
    win = GraphWin("Dice", 320, 240)
    for i in range (1, 125, 25): #squares
        top = 1
        bottom = 25
        die = Rectangle(Point(i, top), Point(i+25, bottom))
        die.draw(win)
    for i in range (30, 125, 25): #upper left dots
        dot = Circle(Point(i, 5), 2)
        dot.setFill("black")
        dot.draw(win)
    for i in range (45, 125, 25): #lower right dots
        dot = Circle(Point(i, 20), 2)
        dot.setFill("black")
        dot.draw(win)
    dot = Circle(Point(63,13), 2) #center dot three
    dot.setFill("black")
    dot.draw(win)
    dot = Circle(Point(113,13), 2) #center dot five
    dot.setFill("black")
    dot.draw(win)
    for i in range (95, 125, 25): #upper right dots
        dot = Circle(Point(i, 5), 2)
        dot.setFill("black")
        dot.draw(win)
    for i in range (80, 125, 25): #lower right dots
        dot = Circle(Point(i, 20), 2)
        dot.setFill("black")
        dot.draw(win)

    straight = 6
    if straight == 1:
        dot = Circle(Point(13, 13), 2)  # center dot three
        dot.setFill("black")
        dot.draw(win)
    else:
        for i in range(5, 25, 8):  # upper left dots
            dot = Circle(Point(i, 5), 2)
            dot.setFill("black")
            dot.draw(win)
        for i in range(5, 25, 8):  # upper left dots
            dot = Circle(Point(i, 20), 2)
            dot.setFill("black")
            dot.draw(win)


    p = win.getMouse()

main()