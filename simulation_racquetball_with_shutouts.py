#rball.py
from random import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB, shutoutsA, shutoutsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB, shutoutsA, shutoutsB)

def printIntro():
    print("This program simulates a game of racquetball between two")
    print('players called "A" and "B".  The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving.  Player A always")
    print("has the first serve.")

def getInputs():
    #Returns the three simulation parameters
    a = eval(input("What is the probability player A wins a serve? "))
    b = eval(input("What is the probability player B wins a serve? "))
    n = eval(input("How many games should we simulate? "))
    return a, b, n

def simNGames(n, probA, probB):
    #Simulates n games of racquetball between players whose
    #abilities are represented by the probability of winning a serve.
    #Returns number of wins for A and B
    winsA = winsB = 0
    shutoutsA = shutoutsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            if scoreA==15 and scoreB==0:
                shutoutsA = shutoutsA+1
            winsA = winsA + 1
        else:
            if scoreB==15 and scoreA==0:
                shutoutsB = shutoutsB+1
            winsB = winsB + 1
    return winsA, winsB, shutoutsA, shutoutsB

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
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    #a and b represent scores for a racquetball game
    #Returns True if the game is over, False otherwise.
    return a==15 or b==15

def printSummary(winsA, winsB, shutoutsA, shutoutsB):
    #Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nGames simulated:", n)
    print("Wins for A: {0} ({1:0.1%}) of which {2:0.1%} are shutouts.".format(winsA, winsA/n, shutoutsA/winsA))
    print("Wins for B: {0} ({1:0.1%}) of which {2:0.1%} are shutouts.".format(winsB, winsB/n, shutoutsB/winsB))

if __name__  == '__main__': main()

