class Card:

    def __init__(self, suit, label):
        self.suit = suit
        self.label = label

    def __str__(self):
        return "(" + self.suit + ": " + self.label + ")"


