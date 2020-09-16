#gpa.py
#Program to find student with highest GPA

class Student:
    def __init__(self, name, hours, qpoints):
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def addGrade(self, gradePoint, credits):
        self.hours += float(credits)
        self.qpoints += float(credits) * float(gradePoint)

    def addLetterGrade(self, grade, credits):
        self.hours += float(credits)
        if(grade=="A"):
            self.qpoints += float(credits) * float(4.0)
        elif(grade=="A-"):
            self.qpoints += float(credits) * float(3.7)
        elif(grade=="B+"):
            self.qpoints += float(credits) * float(3.3)
        elif(grade=="B"):
            self.qpoints += float(credits) * float(3.0)
        elif(grade=="B-"):
            self.qpoints += float(credits) * float(2.7)
        elif(grade=="C+"):
            self.qpoints += float(credits) * float(2.3)
        elif(grade=="C"):
            self.qpoints += float(credits) * float(2.0)
        elif(grade=="C-"):
            self.qpoints += float(credits) * float(1.7)
        elif(grade=="D+"):
            self.qpoints += float(credits) * float(1.3)
        elif(grade=="D"):
            self.qpoints += float(credits) * float(1.0)
        elif(grade=="D-"):
            self.qpoints += float(credits) * float(0.7)
        elif(grade=="F"):
            self.qpoints += float(credits) * float(0.5)

    def getName(self):
        return self.name

    def gethours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints/self.hours



def makeStudent(infoStr):
    # infoStr is a tab-separated line:  name hours qpoints
    # returns a corresponding Student object
    name, hours, qpoints = infoStr.split("\t")
    return Student(name, hours, qpoints)

def main():
    # open the input file for reading
    filename = input("Enter the name of the grade file: ")
    infile = open(filename, 'r')

    # set best to the record for the first student in the file
    best = makeStudent(infile.readline())

    # process subsequent lines of the file
    for line in infile:
        #return the line into a student record
        s = makeStudent(line)
        # if this student is best so far, remember it.
        if s.gpa() > best.gpa():
            best = s
    infile.close()

    # print information about the best student
    print("The best student is:", best.getName())
    print("hours:", best.getHours())
    print("GPA:", best.gpa())

if __name__ == '__main__':
    main()





