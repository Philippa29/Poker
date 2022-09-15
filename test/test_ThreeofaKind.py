import unittest
from Poker.Card import Card
from Poker.Evaluator import Evaluator

"""Unit test for the Straight Hand scenario"""

class Straight_Flush(unittest.TestCase):

    def test_straight_flush(self):
        # Arrange
        print("Shuffling the deck...")
        self.hand=[
            Card(3,7),
              Card(3,7),
              Card(3,7),
              Card(1,13),
              Card(3,3)
              ]
        # Act
        print("your hand is: ", self.hand)
        evaluator = Evaluator(self.hand)
        # Assert
        self.assertEqual(evaluator.check_three_of_a_kind(), True)
        evaluator.check_hand()

if __name__ == "__main__":
    unittest.main()