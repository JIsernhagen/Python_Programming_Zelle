def senator(age, citizenship):
    if age>=30 and citizenship >=9:
        senator = "eligible"
    else:
        senator = "ineligible"
    return senator

def representative(age, citizenship):
    if age>=25 and citizenship >=7:
        representative = "eligible"
    else:
        representative = "ineligible"
    return representative

def main():
    age, citizenship = eval(input("Please input age and duration of citizenship: "))
    print("You are " + senator(age, citizenship) + " to be a senator and " + representative(age, citizenship) + " to be a representative.")

main()