def pay(hours, baserate):
    if (hours<=40):
        pay = hours * baserate
    else:
        pay = (40 * baserate) + ((hours - 40) * (baserate * 1.5))
    return pay

def main():
    hours, baserate = eval(input("Please input hours and hourly rate: "))
    print ("Total pay: " + str(pay(hours, baserate)))

main()