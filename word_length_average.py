def main():
    sentence = input("Please input sentence: ")
    characters = len(sentence) - 1
    spaces = 0
    for ch in sentence:
        if ord(ch) == 32:
            spaces+=1
            characters-=1
    length_avg = characters / (spaces + 1)
    print("This sentence's average word length is {0} characters".format(length_avg))

main()