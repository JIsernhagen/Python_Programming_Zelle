def main():
    n = eval(input("Specify count in sequence: "))
    total = 0
    for i in range(1, n + 1):
        element = eval(input("Input element #"))
        total = total + element
    print("Avg of series= ", total/(n))

main()