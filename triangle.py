import math

def triangle(a, b, c):
    s = (a + b + c) / 2
    triangle = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return triangle

def main():
    import math
    a, b, c = eval(input("Input triangle side lengths: "))
    print("Area of triangle is: ", triangle(a, b, c))

main()