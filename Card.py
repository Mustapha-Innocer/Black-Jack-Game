from Suit import Suit
from Label import Label


class Card:

    def __init__(self, suit, label):
        self.suit = suit
        self.label = label

    def getSuit(self):
        return self.Suit

    def getLabel(self):
        return self.label

    def __str__(self):
        return "(" + self.suit + ": " + self.label + ")"


# newCard = Card(Suit.suits, Label.labels)
#
# newDict = {}
#
# for items in newCard:
#     newCard[items] = Label.labels.keys()
#
#
#
# print(items)

