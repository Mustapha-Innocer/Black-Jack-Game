from .Card import Card


class Player:
    count = 0

    def __init__(self, name, card1: Card, card2: Card):
        self.cards = [card1, card2]
        self.name = name
        self.status = None
        self.count += 1

    def total(self):
        values = [card.point for card in self.cards]
        return sum(values)

    def receive_card(self, card: Card):
        return self.cards.append(card)