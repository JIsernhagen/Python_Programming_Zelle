import math

def sphere_area(radius):
    sphere_area = 4*math.pi*radius**2
    return sphere_area

def sphere_volume(radius):
    sphere_volume = (4 / 3) * math.pi * radius ** 3
    return sphere_volume

def main():
    radius = eval(input("Input radius:"))
    print("Volume: ", sphere_volume(radius))
    print("Area: ", sphere_area(radius))

main()