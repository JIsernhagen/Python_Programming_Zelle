#rball.py
from random import random

def main():
    printIntro()
    probA, probB, matches = getInputs()
    winsA, winsB = simNMatches(matches, probA, probB)
    #winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB, matches)

def printIntro():
    print("This program simulates a set of three-game matches game of racquetball between two")
    print('players called "A" and "B".  The ability of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving.  Player A serves odd games of match.")

def getInputs():
    #Returns the three simulation parameters
    a = eval(input("What is the probability player A wins a serve? "))
    b = eval(input("What it the probability player B wins a serve? "))
    matches = eval(input("How many matches of three games each should we simulate? "))
    return a, b, matches

def simNMatches(matches, probA, probB):
    #Simulates n matches of three games each
    matchwinsA = matchwinsB = 0
    for i in range(matches):
        print("Match: "+ str(i))
        winsA = winsB = 0
        for j in range(3):
            print("Game: "+ str(j))
            if j%2==0:
                serving="B"
            else:
                serving="A"
            scoreA, scoreB = simOneGame(probA, probB, serving)
            if scoreA > scoreB:
                winsA = winsA + 1
                print("A won game")
            else:
                winsB = winsB + 1
                print("B won game")
            if winsA == 2:
                matchwinsA = matchwinsA + 1
                print("A won match")
                break
            if winsB == 2:
                matchwinsB = matchwinsB + 1
                print("B won match")
                break
    print("matchwins A: " +str(matchwinsA) + ", matchwins B: " + str(matchwinsB))
    return matchwinsA, matchwinsB

def simOneGame(probA, probB, serving):
    #Simulates a single game of racquetball between players whose
    #abilities are represented by the probability of winning a serve.
    #Returns the final scores for A and B
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
    print("Score: A: " + str(scoreA) + ", B: " + str(scoreB))
    return scoreA, scoreB

def gameOver(a, b):
    #a and b represent scores for a racquetball game
    #Returns True if the game is over, False otherwise.
    return a==15 or b==15

def printSummary(winsA, winsB, matches):
    #Prints a summary of wins for each player.
    n = winsA + winsB
    print("\nMatches simulated:", matches)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/matches))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/matches))

def simNGames(n, probA, probB):
    #Simulates n games of racquetball between players whose
    #abilities are represented by the probability of winning a serve.
    #Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsA + 1
    return winsA, winsB

if __name__  == '__main__': main()

