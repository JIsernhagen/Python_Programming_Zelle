def acronym(phrase):
    phrase_split = phrase.split(" ")
    acronym = ''
    print(phrase_split)
    for word in phrase_split:
        letter = word[0]
        acronym = acronym + letter.capitalize()
    return acronym


def main():
    phrase = input("Please input phrase to be acronymed: ")
    print("Acronym is: {0}".format(acronym(phrase)))

main()
