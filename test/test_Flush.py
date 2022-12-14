import unittest
from Poker.Card import Card
from Poker.Evaluator import Evaluator

"""Unit test for the Straight Hand scenario"""

class Straight_Flush(unittest.TestCase):

    def test_straight_flush(self):
        # Arrange
        print("Shuffling the deck...")
        print()
        self.hand=[
            Card(3,13),
              Card(3,10),
              Card(3,8),
              Card(3,7),
              Card(3,5)
              ]
        # Act
        print("your hand is: ", self.hand)
        print()
        evaluator = Evaluator(self.hand)
        # Assert
        self.assertEqual(evaluator.check_flush(), True)
        evaluator.check_hand()
        print()

if __name__ == "__main__":
    unittest.main()