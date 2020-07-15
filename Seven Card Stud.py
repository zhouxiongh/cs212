# CS 212, hw1-1: 7-card stud
#
# -----------------
# User Instructions
#
# Write a function best_hand(hand) that takes a seven
# card hand as input and returns the best possible 5
# card hand. The itertools library has some functions
# that may help you solve this problem.
#
# -----------------
# Grading Notes
# 
# Muliple correct answers will be accepted in cases 
# where the best hand is ambiguous (for example, if 
# you have 4 kings and 3 queens, there are three best
# hands: 4 kings along with any of the three queens).

import itertools
import pocker

def best_hand(hand):
    "From a 7-card hand, return the best 5 card hand."
    
    # Your code here
    
    
def test_best_hand():
    assert (sorted(best_hand("6C 7C 8C 9C TC 5C JS".split()))
            == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_hand("TD TC TH 7C 7D 8C 8S".split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_hand("JD TC TH 7C 7D 7S 7H".split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_hand passes'

print test_best_hand()