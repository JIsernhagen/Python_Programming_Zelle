def quiz_grade(score):
    if score ==5:
        quiz_grade = 'A'
    elif score ==4:
        quiz_grade = 'B'
    elif score ==3:
        quiz_grade = 'C'
    elif score ==2:
        quiz_grade = 'D'
    else:
        quiz_grade = 'F'
    return quiz_grade

def main():
    score = eval(input("Please submit quiz score: "))
    print("Quiz grade = "+ quiz_grade(score))

main()