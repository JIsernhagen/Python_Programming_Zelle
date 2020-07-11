def leap_year(year):
    if year%4 == 0:
        if year%400 == 0:
            leap_year = "is not"
        else:
            leap_year = "is"
    else:
        leap_year = "is not"
    return leap_year

def main():
    year = eval(input("Please input year: "))
    print("Year " + str(year) + " " + leap_year(year) + " a leap year.")

main()