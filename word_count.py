def main():
    print("This program calculates number of lines, words and characters.")
    infile_name = input("Please enter the input filename: ")
    input_file = open(infile_name, "r")
    glob = input_file.read()
    lines = 1
    words = 1
    characters = 0
    for ch in glob:
        if ch == '\n':
            lines += 1
            words += 1
        elif ch == " ":
            words += 1
        else:
            characters += 1

    print("Lines: {0}, Words: {1}, Characters: {2}".format(lines, words, characters))
    input_file.close


main()