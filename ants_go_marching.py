def ants_go_marching(count):
    print("The ants to marching {0} by {0}, hurrah! hurrah!".format(count))

def action(count, phrase):
    print("The ants to marching {0} by {0}".format(count))
    print("The little one stops to {0} ".format(phrase))
    print("And they all go marching down to the ground")
    print("to get out of the rain, BOOM! BOOM! BOOM!")

def verse(count, phrase):
    ants_go_marching(count)
    ants_go_marching(count)
    action(count, phrase)
    print()

def main():
    verse("one", "suck his thumb")
    print()
    verse("two", "tie his shoe")
    print()
    verse("three", "climb a tree")
    print()
    verse("four", "shut the door")
    print()
    verse("five", "take a dive")
    print()
    verse("six", "pick up sticks")
    print()
    verse("seven", "pray to heaven")
    print()
    verse("eight", "roller skate")
    print()
    verse("nine", "check the time")
    print()
    verse("ten", "shout 'The End!'")


main()