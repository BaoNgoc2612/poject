
class Card:
    def __init__(self, suit, value):
        self.suit = suit #self.suit la ten thuoc tinh 
        self.value = value #suit la gia tri 
         
    def print_value_card(self):
        print(f"{self.value} of {self.suit}")
def card():
    #cards = []
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    #for suit in suits:
     #   for value in values:
     #       cards.append(deck_of_cards(suit, value))
    #for card in cards:
      #  print(card)
    for i in range(len(suits)):
        for j in range(len(values)):
            f = Card(suit = suits[i], value = values[j])
            f.print_value_card()
    
card()


    

    
