import math

def pizzaarea(radius):
    pizzaarea = math.pi*radius**2
    return pizzaarea

def pizzacostpersquareinch(radius, price):
    pizzacostpersquareinch = price / pizzaarea(radius)
    return pizzacostpersquareinch

def main():
    diameter, price = eval(input("Input pizza diameter and price: "))
    radius = diameter / 2
    print("The cost per square inch of the pizza is: {0}".format(pizzacostpersquareinch(radius, price)))

main()