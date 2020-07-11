from random import *

def main():
    same = 0
    n = eval(input("Please input number of throw attempts: "))
    for i in range(n):
        dierolls = []
        for j in range(5):
            dierolls.append(dieroll())
        if all_same(dierolls):
            same+=1
    print("All five dice were the same " + str(same) + " out of " + str(n) + " rolls.")

def dieroll():
    roll = random()
    if roll <= 0.1666667:
        return 1
    elif roll <= .3333334:
        return 2
    elif roll <= .5:
        return 3
    elif roll <= .6666667:
        return 4
    elif roll <= .833333:
        return 5
    else:
        return 6

def all_same(items):
    return all(x == items[0] for x in items)

main()