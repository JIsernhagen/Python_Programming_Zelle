def main():
    n = eval(input("Please input any integer: "))
    for i in range (2, n):
        if n%i == 0:
            print(str(n) + " is not prime:  divisible by: " + str(i))
            exit()
    print(str(n) + " is prime.")

main()