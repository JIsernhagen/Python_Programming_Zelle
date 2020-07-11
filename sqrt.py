import math

def nextGuess(guess, x):
    betterguess = (guess + (x/guess))/2
    return betterguess

def main():
    x, guess, iterations  = eval(input("Input the number you want square rooted, your guess and number of Newton iterations: "))
    for i in range(0,iterations):
        print("For iteration " + str(i+1) + " betterguess =" , nextGuess(guess, x))
        print("Error =" , math.sqrt(x) - nextGuess(guess, x))
        guess = nextGuess(guess, x)

main()