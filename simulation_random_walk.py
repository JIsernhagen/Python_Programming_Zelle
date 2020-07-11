from random import *

def main():
    position = 0
    n = eval(input("Please input number of steps: "))
    for i in range(n):
        position += step()
    print("Final position after " + str(n) + " steps is " + str(position) + ".")

def step():
    step = random()
    if step <= 0.5:
        return -1
    else:
        return 1

main()