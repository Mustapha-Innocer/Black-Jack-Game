class Card:

    def __init__(self, suit, label):
        self.suit = suit
        self.label = label

        if label == 'ace':
            self.point = 11
        elif label in ['king', 'queen', 'jack']:
            self.point = 10
        else:
            self.point = int(label)

    def __str__(self):
        return "(" + self.suit + ": " + self.label + ")"
