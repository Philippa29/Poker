import unittest
from Poker.Card import Card
from Poker.Evaluator import Evaluator

"""Unit test for the Straight Hand scenario"""

class Straight_Flush(unittest.TestCase):

    def test_straight_flush(self):
        # Arrange
        print(" ")
        print("Shuffling the deck...")
        self.hand=[
            Card(3,10),
              Card(1,9),
              Card(2,8),
              Card(0,7),
              Card(3,6)
              ]
        # Act
        print("your hand is: ", self.hand)
        evaluator = Evaluator(self.hand)
        # Assert
        self.assertEqual(evaluator.check_straight(), True)
        evaluator.check_hand()

if __name__ == "__main__":
    unittest.main()