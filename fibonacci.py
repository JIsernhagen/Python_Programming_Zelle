def fibonacci_calc(n):
    list = [0, 1]
    for i in range(1, n):
        nextterm = list[-2] + list[-1]
        print(nextterm)
        list.append(nextterm)
    fibonacci_calc = list[-1]
    return fibonacci_calc

def main():
    n = eval(input("Please input number: "))
    print(fibonacci_calc(n))

main()