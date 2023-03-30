import random
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
shuffle = [suits, values]
random.choices(shuffle)

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.cards = []   
    def __str__(self):
        return f"{self.value} of {self.suit}"
class Deck:
    def __init__(self):
        self.cards = []
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))
deck = Deck()
for card in deck.cards:
    print(card)