# button_round.py
from graphics import *
from math import sqrt

class Button_round:

    """A button_round is a labeled circle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods.  The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, radius, label):
        """ Creates a circular button, eg:
        qb = Button(myWin, centerPoint, radius, 'Quit') """

        self.x, self.y = center.getX(), center.getY()
        self.circle = Circle(center, radius)
        self.radius = radius
        #self.x = x
        #self.y = y
        self.circle.setFill('lightgray')
        self.circle.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and self.radius >= sqrt((p.getX()-self.x)**2 + (p.getY()-self.y)**2))

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        #self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        #self.rect.setWidth(1)
        self.active = False
