import unittest
from Poker.Card import Card
from Poker.Evaluator import Evaluator

"""Unit test for the One Pair scenario"""

class Straight_Flush(unittest.TestCase):

    def test_straight_flush(self):
        # Arrange
        print("Shuffling the deck...")
        self.hand=[
            Card(3,14),
              Card(1,14),
              Card(2,13),
              Card(0,10),
              Card(3,7)
              ]
        # Act
        print("your hand is: ", self.hand)
        evaluator = Evaluator(self.hand)
        # Assert
        self.assertEqual(evaluator.check_one_pairs(), True)
        evaluator.check_hand()

if __name__ == "__main__":
    unittest.main()