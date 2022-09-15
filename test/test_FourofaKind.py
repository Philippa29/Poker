import unittest
from Poker.Card import Card
from Poker.Evaluator import Evaluator

"""Unit test for the Straight Hand scenario"""

class Four_of_a_Kind(unittest.TestCase):

    def test_Four_of_a_Kind(self):
        # Arrange
        print("Shuffling the deck...")
        self.hand=[
            Card(3,11),
            Card(2,11),
            Card(1,11),
            Card(0,11),
            Card(3,7)
              ]
        # Act
        print("your hand is: ", self.hand)
        evaluator = Evaluator(self.hand)
        # Assert
        self.assertEqual(evaluator.check_four_of_a_kind(), True)
        evaluator.check_hand()

if __name__ == "__main__":
    unittest.main()