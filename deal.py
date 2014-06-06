import random
import poker as pkr

"""Builds a deck of 52 cards.
Rnadom library for shuffling cards."""

# List comprehensions
mydeck = [r+s for r in '23456789TJQKA' for s in 'SJDC']

hand_names = ['Straight Flush',
              '4 Kind',
              'Full House',
              'Flush',
              'Straight',
              '3 Kind',
              '2 Pair',
              'Pair',
              'High Card']


def deal(numhands, n=5, deck=mydeck):
    "Shuffle the deck and deal out n-cards for numhands-times from mydeck"
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]


def hand_percentages(n=700*1000):
    "Sample n random hands and print a table of percentages for each hand."
    counts = [0] * 9
    for i in range(n/10):
        for hand in deal(10):
            ranking = pkr.hand_rank(hand)[0]
            counts[ranking] += 1
    for i in reversed(range(9)):
        print("%14s: %6.3f %%" % (hand_names[i], 100.*counts[i]/n))

if __name__ == '__main__':
    # print(deal(2))
    hand_percentages()

