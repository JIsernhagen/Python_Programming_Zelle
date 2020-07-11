def main():
    print("This program illustrates a chaotic function")
    #n = eval(input("How many numbers should I print? "))
    x, y = eval(input("Enter two number between 0 and 1: "))
    print("index        {0:0.5f}           {1:0.5f}".format(x, y))
    print("------------------------------------------")
    for i in range(10):
        x = 3.9 * x -3.9 * x * x
        y = 3.9 * y -3.9 * y * y
        print("{0:2}            {1:0.5f}           {2:0.5f}".format(i+1, x, y))


main()