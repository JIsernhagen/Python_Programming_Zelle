def exam_grade(score):
    if score >=90:
        exam_grade = 'A'
    elif score >=80:
        exam_grade = 'B'
    elif score >=70:
        exam_grade = 'C'
    elif score >=60:
        exam_grade = 'D'
    else:
        exam_grade = 'F'
    return exam_grade

def main():
    score = eval(input("Please submit exam score: "))
    print("Exam grade = "+ exam_grade(score))

main()