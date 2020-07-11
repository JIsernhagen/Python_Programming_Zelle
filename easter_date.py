def easter(year):
    a = year%19
    b = year%4
    c = year%7
    d = (19*a + 24)%30
    e = (2*b + 4*c + 6*d +5)%7
    weirdyears = [1954, 1981, 2049, 2076]
    easter_date = 22 + d + e
    if year in weirdyears:
        easter_date = easter_date - 7
    if easter_date > 31:
        easter = "April " + str(easter_date - 31)
    else:
        easter = "March " + str(easter_date)
    return easter

def main():
    year = eval(input("Please input year for which to calculate Easter: "))
    print("For " + str(year) + " Easter falls on " + easter(year) + ".")

main()