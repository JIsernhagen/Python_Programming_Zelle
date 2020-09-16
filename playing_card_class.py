class card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suit

    def BJValue(self, rank):
        if rank >= 10:
            BJValue = 10
        else:
            BJValue = self.rank
        return BJValue

    def __str__(self):
        if self.rank == 1:
            rankname = 'Ace'
        elif self.rank == 13:
            rankname = 'King'
        elif self.rank == 12:
            rankname = 'Queen'
        elif self.rank == 11:
            rankname = 'Jack'
        else:
            rankname = str(self.rank)

        if self.suit == 'd':
            suitname = 'Diamonds'
        elif self.suit == 'c':
            suitname = 'Clubs'
        elif self.suit == 'h':
            suitname = 'Hearts'
        elif self.suit == 's':
            suitname = 'Spades'
        else:
            suitname = 'Suit not specified'

        return rankname + ' of ' + suitname