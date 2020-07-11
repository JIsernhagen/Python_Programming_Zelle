def speeding_fine(speed, limit):
    if speed > limit:
        if speed >90:
            speeding_fine = 250 + ((speed - limit) * 5)
        else:
            speeding_fine = 50 + (speed - limit) * 5
    else:
        speeding_fine = "Not speeding"
    return str(speeding_fine)

def main():
    speed, limit = eval(input("Please input actual (clocked) speed and speed limit: "))
    s = speeding_fine(speed, limit)
    if s.isdigit():
        print("The speeding fine is: "+ str(s))
    else:
        print("The motorist was not speeding.")

main()
