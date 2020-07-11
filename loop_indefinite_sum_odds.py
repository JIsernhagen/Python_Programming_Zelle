def sum_odd(n):
    t = 0
    i = 1
    while i <= n:
        t = t + (2*i) - 1
        i += 1
    return t

def main():
    n = eval(input("Please input a positive integer: "))
    print("Sum is: "+ str(sum_odd(n)) )

main()