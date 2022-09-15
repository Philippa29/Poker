import unittest
from Poker.Card import Card
from Poker.Evaluator import Evaluator

"""Unit test for the Full House scenario"""

class Full_House(unittest.TestCase):

    def test_full_house(self):
        # Arrange
        print("Shuffling the deck...")
        self.hand=[
            Card(3,14),
              Card(1,14),
              Card(2,14),
              Card(0,3),
              Card(3,3)
              ]
        # Act
        print("your hand is: ", self.hand)
        evaluator = Evaluator(self.hand)
        # Assert
        self.assertEqual(evaluator.check_full_house(), True)
        evaluator.check_hand()

if __name__ == "__main__":
    unittest.main()