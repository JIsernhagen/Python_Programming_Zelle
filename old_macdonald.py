def old_macdonald():
    print("Old MacDonald had a farm")

def eigh_igh():
    print("Ee-igh, Ee-igh, Oh!")

def and_on_that(animal):
    print("And on that farm he had a {0}.".format(animal))

def with_a(sound):
    print("With a {0}-{0} here and a {0}-{0} there,".format(sound))
    print("here a {0}, there a {0}, everywhere a {0}-{0}.".format(sound))

def verse(animal, sound):
    old_macdonald()
    eigh_igh()
    and_on_that(animal)
    eigh_igh()
    with_a(sound)
    old_macdonald()
    eigh_igh()

def main():
    verse("cow", "moo")
    print()
    verse("duck", "quack")
    print()
    verse("pig", "oink")
    print()
    verse("horse", "neigh")
    print()
    verse("sheep", "baah")


main()