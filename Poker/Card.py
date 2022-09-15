"""Card class to keep track of the suit and value of a card"""

class Card:
    
    Number = {
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "J",
        12: "Q",
        13: "K",
        14: "A",}

    Type = {
        3: u"\u2665",  # Hearts
        2: u"\u2666",  # Diamonds
        1: u"\u2663",  # Clubs
        0: u"\u2660",  # Spades
        }

   
    def __init__(self, suit, value):
        self.suit = Card.Type[suit]
        self.value = Card.Number[value]

    
    def __repr__(self):
        return f"{self.suit} {self.value} "