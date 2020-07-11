def main():
    divisorlist = []
    n = eval(input("Please input any integer: "))
    for i in range (2, n):
        if n%i == 0:
            divisorlist.append(i)
    if not divisorlist:
        print(str(n) + " is prime.")
    else:
        print("Divisors of " + str(n) + " are:")
        for divisor in divisorlist:
            print(str(divisor))

main()