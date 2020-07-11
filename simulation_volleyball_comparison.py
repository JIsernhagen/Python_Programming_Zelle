from random import *

def main():
    sims = eval(input("Please specify number of simulations for each comparison: "))
    inputfile = input("Please specify name of file serve win probabilities: ") #win_probs.txt
    infile = open(inputfile, 'r')
    for line in infile:
        probA, probB = line.split(" ")
        probA = eval(probA)
        probB = eval(probB)
        a = main15(probA, probB, sims)[0]
        b = main15(probA, probB, sims)[1]
        c = mainrally(probA, probB, sims)[0]
        d = mainrally(probA, probB, sims)[1]
        #print(str(c) + ", " + str(d))
        print("With probability A: {0} and probability B: {1} 15 generates A: {2} ({3:0.1%}) and B: {4} {5:0.1%} and rally generates A: {6} ({7:0.1%}) and B: {8} {9:0.1%}".format(probA, probB, a, a/sims, b, b/sims, c, c/sims, d, d/sims))

#15 section
def main15(probA, probB, n):
    winsA, winsB = simNGames15(n, probA, probB)
    return winsA, winsB

def simNGames15(n, probA, probB):
    #Simulates n games of volleyball between teams whose
    #abilities are represented by the probability of acing a serve.
    #Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame15(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneGame15(probA, probB):
    #Simulates a single game of racquetball between players whose
    #abilities are represented by the probability of winning a serve.
    #Returns the final scores for A and B
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver15(scoreA, scoreB):
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

def gameOver15(a, b):
    #a and b represent scores for a volleyball game
    #Returns True if the game is over, False otherwise.
    if (a>=15 or b>=15) and (a-b>1 or b-a>1):
        return True
    else:
        return False

#rally section
def mainrally(probA, probB, n):
    winsA, winsB = simNGamesrally(n, probA, probB)
    return winsA, winsB

def simNGamesrally(n, probA, probB):
    #Simulates n games of volleyball between teams whose
    #abilities are represented by the probability of acing a serve.
    #Returns number of wins for A and B
    winsA = winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGamerally(probA, probB)
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def simOneGamerally(probA, probB):
    #Simulates a single game of racquetball between players whose
    #abilities are represented by the probability of winning a serve.
    #Returns the final scores for A and B
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOverrally(scoreA, scoreB):
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

def gameOverrally(a, b):
    #a and b represent scores for a volleyball game
    #Returns True if the game is over, False otherwise.
    if (a>=21 or b>=21) and (a-b>1 or b-a>1):
        return True
    else:
        return False


main()