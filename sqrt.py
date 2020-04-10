def main():
    import math
    x = eval(input("Input x:"))
    guess = x/2
    for i in range(0, 5):
        betterguess = (guess + (x/guess))/2
        guess = betterguess
    print("betterguess =" , betterguess)
    print("error =" , math.sqrt(x) - betterguess)

main()