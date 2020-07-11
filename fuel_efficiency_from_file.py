def main():
    odometer = []
    gas = []
    inputfile = input("Please input name of file with odometer readings and gas amounts: ")
    infile = open(inputfile, 'r')
    for line in infile:
        odometertemp, gastemp = line[:-1].split(" ")
        #print(line[:-1])
        #print(odometertemp + ", " + gastemp)
        odometer.append(eval(odometertemp))
        gas.append(eval(gastemp))
    for leg, reading in enumerate(odometer):
        if leg > 0:
            print("During leg " + str(leg) + " of the trip, over distance " + str(odometer[leg] - odometer[leg-1]) + " fuel efficiency was " + str(odometer[leg] - odometer[leg-1] / gas[leg]) + " m/g")

main()
