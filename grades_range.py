def grade(score):
    if score >= 90:
        grade = 'A'
    elif score >=80:
        grade = 'B'
    elif score >=70:
        grade = 'C'
    elif score >=60:
        grade = 'D'
    else:
        grade = 'F'
    return grade

def main():
    score = eval(input("Please input score: "))
    print("The grade is: {0}".format(grade(score)))

main()