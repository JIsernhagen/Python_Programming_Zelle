def main():
    x1, y1 = eval(input("Please input X1, Y1: "))
    x2, y2 = eval(input("Please input X2, Y2: "))
    slope = (y2 - y1) / (x2 - x1)
    print("Slope = ", slope)

main()
