def main():
    import math
    n = eval(input("Input element count: "))
    pi = 0
    for i in range(1, n+1):
        denominator = (i * 2) - 1
        print(i, denominator)
        if (i%2 == 0):
            pi -= 4 / denominator
        else:
            pi += 4 / denominator

    print(pi)

main()