def main():
    list = [0, 1]
    n = eval(input("Please input number: "))
    for i in range(1, n):
        nextterm = list[-2] + list[-1]
        list.append(nextterm)
    print(list[-1])
main()