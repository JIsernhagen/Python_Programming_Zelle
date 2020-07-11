def main():
    days_cooling = 0
    days_heating = 0
    while True:
        x = input("Please input an average daily temperature:")
        if x == "": break
        x = eval(x)
        if x < 60:
            days_heating+=60-x
        elif x>80:
            days_cooling+=x-80
    print("Days_heating: " + str(days_heating) + ", and days_cooling = " + str(days_cooling) + ".")

main()