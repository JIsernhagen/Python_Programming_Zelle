def sumN(n):
    s = 0
    for i in range(1,n+1):
        s += i
    return s

def sumNCubes(n):
    s = 0
    for i in range(0,n+1):
        s += i**3
    return s

def main():
    n = eval(input("Please input a number n:"))
    print("Sum of {0} natural numbers = {1}, Sum of cubes is: {2}".format(n,sumN(n),sumNCubes(n)))

main()