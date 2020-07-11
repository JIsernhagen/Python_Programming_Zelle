from graphics import *

def main():
    infile_name = input("Please enter the input filename: ")
    input_file = open(infile_name, "r")
    scores = [0,0,0,0,0,0,0,0,0,0,0,0]
    score_highest = 0
    for score in input_file:
        i = eval(score)
        print(i)
        scores[i] +=1
        if scores[i] > score_highest:
            score_highest = scores[i]
    input_file.close()
    win = GraphWin("Score Distribution", 640, 480)
    win.setCoords(0.0, 0.0, 11, score_highest)
    for i in range(0,11):
        Text(Point(i+.5,0.5),i).draw(win)
        Rectangle(Point(i,0),Point(i+1,scores[i])).draw(win)
    win.getMouse()


main()