from random import *

def main():
    #print("Card: " + str(cardvalue(dealeroutcome())))
    n = eval(input("Please input the number of games to simulate: "))
    print("The dealer busts " + str(dealerbusts(n)) + " of " + str(n) + " games.")

def dealerbusts(n):
    dealerbusts = 0
    for game in range(n):
        dealerbusts +=dealeroutcome()
    return dealerbusts

def card():
    card = random()
    if card <= 0.0769230769230769:
        return "A"
    elif card <= 0.153846153846154:
        return "2"
    elif card <= 0.230769230769231:
        return "3"
    elif card <= 0.307692307692308:
        return "4"
    elif card <= 0.384615384615385:
        return "5"
    elif card <= 0.461538461538462:
        return "6"
    elif card <= 0.538461538461539:
        return "7"
    elif card <= 0.615384615384615:
        return "8"
    elif card <= 0.692307692307692:
        return "9"
    elif card <= 0.769230769230769:
        return "10"
    elif card <= 0.846153846153846:
        return "J"
    elif card <= 0.923076923076923:
        return "Q"
    else:
        return "K"

def cardvalue(card):
    if card in ("J", "Q", "K"):
        return 10
    elif card == "A":
        return 11
    else:
        return card

def dealeroutcome():
    dealercards = []
    dealersum = 0
    aceused = False
    while dealersum <= 16:
        newcard = card()
        dealercards.append(newcard)
        dealersum+=int(cardvalue(newcard))
        if dealersum > 21:
            if "A" in dealercards and aceused == False:
                dealersum-=10
                aceused = True
            else:
                print("Dealer had " + str(dealercards))
                return 1
    print("Dealer had " + str(dealercards))
    return 0

def game():
    if dealerscore() >= playerscore():
        return 0
    else:
        return 1

main()