from Deck import Deck
from FisherYates import FisherYates
from Evaluator import Evaluator
#create a player 


class Game:
    def __init__(self):
        self.deck = Deck()
        self.shuffle = FisherYates(self.deck)
    
    def play(self):
        print("Shuffling the deck...")
        hand = self.shuffle.shuffle()
        print("Your hand is: ", hand)
        evaluator = Evaluator(hand)
        evaluator.check_hand()

if __name__ == "__main__":
    game = Game()
    game.play()
    
