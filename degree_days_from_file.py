def main():
    degree_days_heating = 0
    degree_days_cooling = 0
    filename = input("Please input the daily average temperature file name:")
    infile = open(filename, 'r')
    for line in infile:
        x = eval(line)
        if x>80:
            degree_days_heating+=x-80
        elif x<60:
            degree_days_cooling+=60-x
    print("Degree_days_heating = " + str(degree_days_heating) + " and degree_days_cooling = " + str(degree_days_cooling))

main()


