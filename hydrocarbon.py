def main():
    import math
    h = 1.0079
    c = 12.011
    o = 15.9994
    hydrogens = eval(input("Input hydrogens: "))
    carbons = eval(input("Input carbons: "))
    oxygens = eval(input("Input oxygens: "))
    mw = hydrogens * h + carbons * c + oxygens * o
    print("Molecular weight: ", mw)

main()