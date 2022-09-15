from abc import abstractmethod, ABC
from .Card import Card
from .Deck import Deck
from typing import List

"""shuffle class so that the user can change up the type of shuffling ocurring"""
class Shuffle(ABC):

    def __init__(self,deck : Deck):
        self.deck = deck
        self.shuffled_deck = List[Card]

    @abstractmethod
    def shuffle(): 
        pass

    

        
