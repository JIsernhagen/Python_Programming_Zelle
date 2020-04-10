def main():
    import math
    x1, y1 = eval(input("Please input X1, Y1: "))
    x2, y2 = eval(input("Please input X2, Y2: "))
    distance = math.sqrt((y2 - y1)**2 + (x2 - x1)**2)
    print("Distance = ", distance)

main()