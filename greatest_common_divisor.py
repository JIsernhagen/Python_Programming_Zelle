def gcd(m, n):
    for i in range (min(m,n), 1, -1):
        if m%i==0 and n%i==0:
            return i

def main():
    m, n = eval(input("Please input two integers: "))
    print("The greatest common divisor of " + str(m) + " and " + str(n) + " is " + str(gcd(m, n)))

main()