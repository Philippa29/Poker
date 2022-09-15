from .Card import Card
from typing import List
import collections

""" 
    class Evaluator:
    takes in list of cards and returns the best hand
""" 
class Evaluator:
    def __init__(self, hand: List[Card]):
        self.hands = hand

        if(len(self.hands) != 5):
            raise ValueError("Hand must have 5 cards")
        new_hand = []
        for i in range(0,5): 
            if self.hands[i].suit == "♠":
                new_hand.append("S" + self.hands[i].value)
            elif self.hands[i].suit == "♣":
                new_hand.append("C" + self.hands[i].value)
            elif self.hands[i].suit == "♦":
                new_hand.append("D" + self.hands[i].value)
            elif self.hands[i].suit == "♥":
                new_hand.append("H" + self.hands[i].value)
        self.hands = new_hand
    """ 
    class check_flush:
        checks if hand is a flush
        arguments: none 
        returns: boolean
    """    

    def check_flush(self):
        suits = [h[0] for h in self.hands]
        if len(set(suits)) == 1:
            return True
        else:
            return False
    """ 
    class check_straight_flush:
        checks if hand is a straight flush
        arguments: none 
        returns: boolean
    """      
    def check_straight_flush(self):
        if self.check_flush() and self.check_straight():
            return True
        else:
            return False
    """ 
    class check_straight:
        checks if hand is a straight
        arguments: none 
        returns: boolean
    """  
    def check_straight(self):
        rank_values = []
        values = [i[1] for i in self.hands]
        value_counts = collections.defaultdict(lambda:0)
        for v in values:
            value_counts[v] += 1
        for i in values:
            if i == "A":
                rank_values.append(14)
            if i == "K":
                rank_values.append(13)
            if i == "Q":
                rank_values.append(12)
            if i == "J":
                rank_values.append(11)
            if i == "10":
                rank_values.append(10)
            if i == "9":
                rank_values.append(9)
            if i == "8":
                rank_values.append(8)
            if i == "7":
                rank_values.append(7)
            if i == "6":
                rank_values.append(6)
            if i == "5":
                rank_values.append(5)
            if i == "4":
                rank_values.append(4)
            if i == "3":
                rank_values.append(3)
            if i == "2":
                rank_values.append(2)
        value_range = max(rank_values) - min(rank_values)
        if len(set(value_counts.values())) == 1 and (value_range==4):
            return True
        else:
        #check straight with low Ace
            if set(values) == set(["A", "2", "3", "4", "5"]):
                return True
        return False

    """ 
    class check_four_of_a_kind:
        checks if hand is a four of a kind
        arguments: none 
        returns: boolean
    """      
    def check_four_of_a_kind(self):
        values = [i[1] for i in self.hands]
        value_counts = collections.defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if sorted(value_counts.values()) == [1,4]:
            return True
        return False
    """ 
    class check_full_house:
        checks if hand is a full house
        arguments: none 
        returns: boolean
    """  
    def check_full_house(self):
        values = [i[1] for i in self.hands]
        value_counts = collections.defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if sorted(value_counts.values()) == [2,3]:
            return True
        return False
    """ 
    class check_three_of_a_kind:
        checks if hand is a three of a kind
        arguments: none 
        returns: boolean
    """  
    def check_three_of_a_kind(self):
        values = [i[1] for i in self.hands]
        value_counts = collections.defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if set(value_counts.values()) == set([3,1]):
            return True
        else:
            return False
    """ 
    class check_two_pairs:
        checks if hand is a two pairs
        arguments: none 
        returns: boolean
    """  
    def check_two_pairs(self):
        values = [i[1] for i in self.hands]
        value_counts = collections.defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if sorted(value_counts.values())==[1,2,2]:
            return True
        else:
            return False
    """ 
    class check_one_pairs:
        checks if hand is a flush
        arguments: none 
        returns: boolean
    """  
    def check_one_pairs(self):
        values = [i[1] for i in self.hands]
        value_counts = collections.defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if 2 in value_counts.values():
            return True
        else:
            return False
    """ 
    class check_high_card:
        checks if hand is a flush
        arguments: none 
        returns: boolean
    """  
    def check_high_card(self):
        values = [i[1] for i in self.hands]
        value_counts = collections.defaultdict(lambda:0)
        for v in values:
            value_counts[v]+=1
        if 1 in value_counts.values():
            return True
        else:
            return False
    """ 
    class check_hand:
        checks what hand is
        arguments: none 
        prints the type of hand
    """  
    def check_hand(self):
        if self.check_straight_flush():
            print("Straight Flush")
        elif self.check_four_of_a_kind():
            print("Four of a Kind")
        elif self.check_full_house():
            print("Full House")
        elif self.check_flush():
            print("Flush")
        elif self.check_straight():
            print("Straight")
        elif self.check_three_of_a_kind():
            print("Three of a Kind")
        elif self.check_two_pairs():
            print("Two pairs")
        elif self.check_one_pairs():
            print("One pair")
        elif self.check_high_card():
            print("High card")
        else:
            print("Nothing")




