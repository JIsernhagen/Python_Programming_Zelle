def main():
    import math
    a, b, c = eval(input("Input triangle side lengths: "))
    s = (a + b + c) / 2
    A = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print("Area of triangle is: ", A)

main()