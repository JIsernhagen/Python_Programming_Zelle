def log2n(n):
    i = 0
    while n > 1:
        n = n / 2
        i+=1
    return i

def main():
    n = eval(input("Please input a number: "))
    print("Iterations = :"+str(log2n(n)))

main()