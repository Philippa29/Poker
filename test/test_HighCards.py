import unittest
from Poker.Card import Card
from Poker.Evaluator import Evaluator

"""Unit test for the Straight Hand scenario"""

class Straight_Flush(unittest.TestCase):

    def test_straight_flush(self):
        # Arrange
        print("Shuffling the deck...")
        self.hand=[
            Card(3,13),
              Card(1,8),
              Card(2,12),
              Card(0,2),
              Card(3,7)
              ]
        # Act
        print("your hand is: ", self.hand)
        evaluator = Evaluator(self.hand)
        # Assert
        self.assertEqual(evaluator.check_high_card(), True)
        evaluator.check_hand()

if __name__ == "__main__":
    unittest.main()