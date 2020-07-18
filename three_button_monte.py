#three-button-monte game, original simple version
#draws three buttons labeled "door 1," "door 2," "door 3"
#user is prompted and selects one of the buttons
#user clicks one of the buttons and is advised whether he/she won or lost.

from graphics import *
from random import randrange
from button import Button

def main():
    #create the application window
    win = GraphWin("Three Button Monte")
    win.setCoords(0, 0, 22, 10)
    win.setBackground("green2")
    width = 6
    height = 4

    #Draw buttons
    door1 = Button(win, Point(4,7.5), width, height, 'Door\n 1')
    door1.activate()
    door2 = Button(win, Point(11,7.5), width, height, 'Door\n 2')
    door2.activate()
    door3 = Button(win, Point(18,7.5), width, height, 'Door\n 3')
    door3.activate()
    label = Text(Point(11,3), 'Choose a door.').draw(win)
    doorprize = randrange(1,4)
    print('door = ' + str(doorprize))

    x = win.getMouse()
    print(x)
    if (door1.clicked(x) == 1 and doorprize ==1) or (door2.clicked(x) == 1 and doorprize ==2) or (door3.clicked(x) == 1 and doorprize ==3):
        label.setText('You win!')
    elif (door1.clicked(x) == 1 and doorprize !=1) or (door2.clicked(x) == 1 and doorprize !=2) or (door3.clicked(x) == 1 and doorprize !=3):
        label.setText('You lose, the correct \n door was: #' + str(doorprize))
    else:
        label.setText('You missed.')

    z = win.getMouse()

main()