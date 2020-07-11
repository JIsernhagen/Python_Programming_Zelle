from random import *

def main():
    wins = 0
    n = eval(input("Please input desired number of games: "))
    for i in range(n):
        wins+=crapsgame()
    print("Win percentage: " + str(wins/n))


def crapsgame():
    #initial roll
    initialroll = dieroll() + dieroll()
    print("Initial roll: " + str(initialroll))
    if initialroll in (2, 3, 12):
        print("Rolled " + str(initialroll) + " and lost.")
        return 0
    elif initialroll in (7, 11):
        print("Rolled " + str(initialroll) + " and won.")
        return 1
    else:
        print("Rolling for point")
        while True:
            pointroll = dieroll() + dieroll()
            if pointroll == initialroll:
                print("Rolled another " + str(initialroll) + " to win!")
                return 1
                break
            elif pointroll == 7:
                print("Rolled a 7 and crapped out.")
                return 0
                break


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

main()