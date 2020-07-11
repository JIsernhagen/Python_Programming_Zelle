import datetime

def babysitting_fee(starttime, endtime):
    bedhour = 21
    starthour, startminute = starttime.split(":")
    endhour, endminute = endtime.split(":")
    startfraction = int(starthour) + int(startminute)/60
    endfraction = int(endhour) + int(endminute)/60
    if (startfraction <= bedhour) and  (bedhour <= endfraction): #span
        babysitting_fee = ((bedhour - startfraction) * 2.50) + ((endfraction - bedhour) * 1.75)
    elif (startfraction <= bedhour) : #early
        babysitting_fee = ((bedhour - startfraction) * 2.50)
    elif (bedhour <= endfraction): #late
        babysitting_fee = ((endfraction - bedhour) * 1.75)
    else:
        babysitting_fee = "Cannot be computed"
    return str(babysitting_fee)

def main():
    starttime = input("Please input start time in HH:MM format: ")
    endtime = input("Please input end time in HH:MM format: ")
    b = babysitting_fee(starttime, endtime)
    if b =='Cannot be computed':
        print("The fee cannot be calculated.")
    else:
        print("The fee is: $"+ str(b))


main()