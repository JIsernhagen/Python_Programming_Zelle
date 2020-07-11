def square(n):
    square = n**2
    return square

def main():
    infile_name = input("Please enter the input filename: ")
    input_file = open(infile_name, "r")
    glob = input_file.readlines()
    s = 0
    for line in glob:
        s+=eval(line)

    input_file.close
    print("Sum of squares of the numbers from the input file is: "+str(s))

main()