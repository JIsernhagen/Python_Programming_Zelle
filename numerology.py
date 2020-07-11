def acronym()

def main():
    name = input("Please input name: ")
    name = name.lower()
    total = 0
    for ch in name:
        if ord(ch) != 32:
            total = total + (ord(ch) - 96)
    print("Total is {0}".format(total))

main()