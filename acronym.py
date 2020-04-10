def main():
    phrase = input("Please input phrase to be acronymed: ")
    phrase_split = phrase.split(" ")
    acronym = ''
    print(phrase_split)
    for word in phrase_split:
        letter = word[0]
        acronym = acronym + letter.capitalize()
    print("Acronym is: {0}".format(acronym))

main()
