def fibonacci_loop(n):
    f_1 = 0
    f = 1
    for i in range(n-1):
        fnew = f_1 + f
        f_1 = f
        f = fnew
    return f

def main():
    n = eval(input("Please input a number n: "))
    print("The fibonacci number for " + str(n) + " is " + str(fibonacci_loop(n)))

main()