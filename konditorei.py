def main():
    c = 10.50
    s = 0.86
    f = 1.50
    lbs = eval(input("Please input number of pounds in order: "))
    oc = 1.50 + lbs * (c + s)
    print("Order cost is: ", oc)

main()