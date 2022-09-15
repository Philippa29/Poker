from .Card import Card
import itertools
from typing import List

""" Deck class to create the 52 card deck"""

class Deck:
    def __init__(self):
        self.cards = List[Card]
        self.cards = [Card(suit, value) for suit, value in itertools.product(range(4), range(2,15))]







