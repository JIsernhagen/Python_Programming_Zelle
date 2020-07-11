def leap_year(year):
    if year%4 == 0:
        if year%400 == 0:
            leap_year = "is not"
        else:
            leap_year = "is"
    else:
        leap_year = "is not"
    return leap_year

def date_valid(month, day, year):
    if 1<=month<=12:
        if ((month in [4, 6, 9, 11]) and (1 <= day <= 30)) or ((month in [1, 3, 5, 7, 8, 10, 12]) and (1 <= day <= 31)) or (month == 2 and 1<=day<=28) or ((month == 2 and day == 29 and leap_year(year) == "is")):
            date_valid = "legit"
        else:
            date_valid = "not legit"
    else:
        date_valid = "not legit"
    return date_valid

def dayNum(month, day, year):
    dayNum = 31*(month-1) + day
    if month >=3:
        dayNum = dayNum - ((4*month)+23)//10
    if (leap_year(year) and month > 2):
        dayNum = dayNum + 1
    return dayNum

def main():
    monthtext, daytext, yeartext = input("Please input the month, day and year in M/D/Y format: ").split("/")
    month = int(monthtext)
    day = int(daytext)
    year = int(yeartext)
    if date_valid(month, day, year) == 'legit':
        print("The calculated day number is: " + str(dayNum(month, day, year)))
    else:
        print('The date you entered was not in a valid format.  Please try again.')

main()
