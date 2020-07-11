from graphics import *

def main():
    infile_name = input("Please enter the input filename: ")
    input_file = open(infile_name, "r")
    students = eval(input_file.readline())
    win = GraphWin("Scores", 640, 480)
    win.setCoords(-20.0, 0.0, 110, students)
    student = 1
    for line in input_file:
        name, score = line.split(" ")
        Text(Point(-10,student + 0.5),name).draw(win)
        Rectangle(Point(0,student),Point(score, student+1)).draw(win)
        student+=1
    input_file.close()
    win.getMouse()


main()