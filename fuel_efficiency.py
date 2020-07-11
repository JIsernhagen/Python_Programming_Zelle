def main():
    odometer = []
    gas = []
    odometerstart = eval(input("Please input starting odometer reading: "))
    odometer.append(odometerstart)
    while True:
        odometergas = input("Please input successive odometer reading and gas used, separated by space: ")
        if odometergas == "": break
        odometertemp, gastemp = odometergas.split(" ")
        odometer.append(eval(odometertemp))
        gas.append(eval(gastemp))
    for leg, reading in enumerate(gas):
        print("During leg " + str(leg + 1) + " of the trip, over distance " + str(odometer[leg+1] - odometer[leg]) + " fuel efficiency was " + str(odometer[leg+1] - odometer[leg] / gas[leg]) + " m/g")

main()
