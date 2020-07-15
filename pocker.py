import random

def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return allmax(hands, key=hand_rank)

def allmax(iterable, key = None):
    re = []
    for i in iterable:
        if hand_rank(max(iterable, key = hand_rank)) == hand_rank(i):
            re.append(i)
    return re

def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6,kind(3, ranks), kind(2, ranks))# your code here
    elif flush(hand):                              # flush
        return (5,ranks)# your code here
    elif straight(ranks):                          # straight
        return (4,max(ranks))# your code here
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks),ranks)# your code here
    elif two_pair(ranks):                          # 2 pair
        return (2,two_pair(ranks),ranks)# your code here
    elif kind(2, ranks):                           # kind
        return (1,kind(2,ranks),ranks)# your code here
    else:                                          # high card
        return (0,ranks)# your code here

def card_ranks(cards):
    ranks = ['--23456789TJQA'.index(r) for r, s in cards]
    ranks.sort(reverse = True)
    return ranks

def straight(cards):
    return max(cards) - min(cards) == 4 and len(set(cards)) == 5

def flush(cards):
    a = cards[0][1]
    for e in cards:
        if e[1] != a:
            return False
    return True

def kind(n, ranks):
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None

def two_pair(ranks):
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    return None

mydeck = [r+s for r in '23456789TJQKA' for s in "SHDC"]

def deal(numhands, n = 5, deck = mydeck):
    random.shuffle(mydeck)
    return [mydeck[i*n:(i+1)*n] for i in range(numhands)]
    

def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() 
    fk = "9D 9H 9S 9C 7D".split() 
    fh = "TD TC TH 7C 7D".split()
    tp = "5S 5D 9H 9C 6S".split()
    print(poker([sf, fk, fh]))
    assert poker([sf, fk, fh]) == [sf]
    assert poker([fk, fh]) == [fk]
    assert poker([fh, fh]) == [fh, fh]
    assert poker([fh]) == [fh]
    assert poker([sf] + 99 * [fk]) == [sf]
    # Add 2 new assert statements here. The first 
    # should assert that when poker is called with a
    # single hand, it returns that hand. The second 
    # should check for the case of 100 hands.
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)

    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]

    assert straight([9, 8 ,7 ,6 ,5]) == True
    assert straight([9, 8 ,7 ,6 ,6]) == False
    assert flush(sf) == True
    assert flush(fk) == False

    fkranks = card_ranks(fk)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7

    tpranks = card_ranks(tp)
    assert two_pair(tpranks) == (9, 5)
    return 'tests pass'
    
print(test())