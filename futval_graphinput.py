#futval_graphinput.py

from graphics import *

def main():
    #Introduction
    print("This program plots the growth of a 10-year inveestment.")

    #Create a graphics window with labels on left edge
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")
    win.setCoords(-2, -700, 11.3, 14000)
    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 10000), '10.0K').draw(win)

    #Get principal and interest rate
    Text(Point(0,12500), 'Principal: ').draw(win)
    Text(Point(7,12500),'APR: ').draw(win)
    prin_input = Entry(Point(3.5, 12500), 5).draw(win)
    apr_input = Entry(Point(9,12500),5).draw(win)
    win.getMouse()

    #Conversions
    principal = eval(prin_input.getText())
    apr = eval(apr_input.getText())

    #Draw bar for initial principal
    bar = Rectangle(Point(0,0), Point(1,principal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)

    #Draw a bar for each subsequent year
    for year in range(1, 11):
        principal = principal * (1 + apr)
        bar = Rectangle(Point(year, 0), Point(year+1, principal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)

    input("Press <Enter> to quit.")
    win.close()

main()