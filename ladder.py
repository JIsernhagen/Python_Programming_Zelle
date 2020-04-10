def main():
    import math
    height, angle = eval(input("Pleaes input height and angle of ladder: "))
    radians = math.pi/180 * angle
    length = height / math.sin(radians)
    print("Ladder length: ", length)

main()
