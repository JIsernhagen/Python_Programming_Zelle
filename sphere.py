def main():
    import math
    r = eval(input("Input radius:"))
    v = (4/3)*math.pi*r**3
    a = 4*math.pi*r**2
    print("Volume: ", v)
    print("Area: ", a)

main()