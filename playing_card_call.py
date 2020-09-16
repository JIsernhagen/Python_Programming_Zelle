from playing_card_class import card
from random import choice, randrange

for i in range(20):
    rank = randrange(1,13)
    suits = ['d', 'c', 'h', 's']
    suit = choice(suits)
    #print(rank)
    #print(suit)
    c = card(rank, suit)
    print(c)
