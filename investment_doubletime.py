def main():
    p = 1
    i = eval(input("Input interest rate: "))
    n = 0
    while p < 2:
        p = p + (p * i)
        n += 1
    print("Doubling periods for " + str(i) + " were " + str(n))


main()
