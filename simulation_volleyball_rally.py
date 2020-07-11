#rball.py
from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)

def printIntro():
    print("This program simulates a game of volleyball between two")
    print('teams called "A" and "B".  The ability of each team is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the server will earn a point on the serve.  Team A always")
    print("has the first serve.")

def getInputs():
    #Returns the three simulation parameters
    a = eval(input("What is the probability team A wins on serve? "))
    b = eval(input("What it the probability team B wins on serve? "))
    n = eval(input("How many games should we simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
    #Simulates n games of volleyball between teams whose
    #abilities are represented by the probability of acing a serve.
    #Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneGame(probA, probB):
    #Simulates a single game of racquetball between players whose
    #abilities are represented by the probability of winning a serve.
    #Returns the final scores for A and B
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                scoreB = scoreB + 1
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                scoreA = scoreA + 1
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    #a and b represent scores for a volleyball game
    #Returns True if the game is over, False otherwise.
    if (a>=21 or b>=21) and (a-b>1 or b-a>1):
        return True
    else:
        return False

def printSummary(winsA, winsB):
    #Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nGames simulated:", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))

if __name__  == '__main__': main()

