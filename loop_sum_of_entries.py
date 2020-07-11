def main():
    t = 0
    while True:
        n = input("Please input a number to sum: ")
        if n == '999': break
        t+= eval(n)
    print("Sum is: "+ str(t))
main()