def main():
    phrase = input("Please input phrase: ")
    spaces = 0
    for ch in phrase:
        if ord(ch) == 32:
            spaces+=1
    print("There are {0} spaces".format(spaces))

main()