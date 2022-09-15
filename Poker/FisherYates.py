from .Shuffle import Shuffle
from .Deck import Deck
from random import randint

class FisherYates(Shuffle):
    
    def __init__(self,deck: Deck):
        super().__init__(deck)
        """ 
    class shuffle:
        checks if hand is a flush
        arguments: none 
        returns: shuffled hand
    """  
    def shuffle(self):
        num_cards = 5
        self.shuffled_deck = self.fisher_yates()
        shuffled_hand = []
        if num_cards < 6 and num_cards > 0:
            for i in range(num_cards):
                shuffled_hand.append(self.deck.cards.pop())
        return shuffled_hand
    """ 
    class fisher_yates:
        does the actual shuffling
        arguments: none 
        returns: shuffled cards
    """  
    def fisher_yates(self):
        cards = self.deck.cards
        for i in range(len(cards) - 1, 0, -1):
            j = randint(0, i)
            cards[i], cards[j] = cards[j], cards[i]
        return cards