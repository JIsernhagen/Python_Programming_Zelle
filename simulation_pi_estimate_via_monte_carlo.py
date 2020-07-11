from random import *
import math

def main():
    h = 0
    n = eval(input("Please input number of darts to throw: "))
    for i in range(n):
        x = 2 * random() - 1
        y = 2 * random() - 1
        #print(str(x) + ", " + str(y))
        if x**2 + y**2 <= 1:
            h +=1
    print("Pi is approximately: " +str((4*h)/n))

main()