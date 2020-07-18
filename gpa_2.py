from gpa import Student, makeStudent


def main():
    # open the input file for reading
    studentname, studenthours, studentqpoints = input("Please input name, hours and quality points of student: ").split(",")
    infoStr = studentname + "\t" + studenthours + "\t" + studentqpoints
    student = makeStudent(infoStr)
    gradePoint, credits = input("Please input gradePoint and credits: ").split(",")
    student.addGrade(gradePoint, credits)
    print()

if __name__ == '__main__':
    main()