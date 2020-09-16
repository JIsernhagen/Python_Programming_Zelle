from gpa import Student, makeStudent


def main():
    # open the input file for reading
    #studentname, studenthours, studentqpoints = input("Please input name, hours and quality points of student: ").split(",")
    #infoStr = studentname + "\t" + studenthours + "\t" + studentqpoints
    student = Student("Adams, Henry", 0, 0)
    gradePoint, credits = ("B",3.0)
    student.addLetterGrade(gradePoint, credits)
    print("Student " + student.getName() + " GPA = " + str(student.gpa()))

if __name__ == '__main__':
    main()