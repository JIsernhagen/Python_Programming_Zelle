def primelist(n):
    primelist = [1]
    for i in range (2, n):
        if isprime(i):
            primelist.append(i)
    return primelist

def isprime(n):
    divisorlist = []
    for i in range(2, n):
        if n % i == 0:
            divisorlist.append(i)
    if not divisorlist:
        return True
    else:
        return False

def main():
    x = 1
    while x % 2 != 0:
        x = eval(input("Please input an even number: "))
    for i in primelist(x):
        for j in primelist(x):
            if i + j == x:
                print("The sum of " + str(i) + " + " + str(j) + " = " + str(x))
                quit()

main()