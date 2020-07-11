from random import *

def main():
    x = 0
    y = 0
    n = eval(input("Please input number of steps: "))
    for i in range(n):
        x += step()[0]
        y += step()[1]
    print("Final position after " + str(n) + " steps is (" + str(x) + ", " + str(y) + ").")

def step():
    step = random()
    if step <= 0.25:
        return 0, 1
    elif step <= .5:
        return 1, 0
    elif step <= .75:
        return -1, 0
    else:
        return 0, -1

main()