# Coin flip program

import random

nFlips = 0 # to count the number of flips

nTails = 0 # to count the number of flips that come up as tails

nHeads = 0 # to count the number of flips that come up as heads

maxFlips = input('How many flips do you want to do? ')
maxFlips = int(maxFlips)

while nFlips < maxFlips:
    # Randomly choose 0 or 1, because a coin flip can only result in one of two answers
    # (heads or tails)

    zeroOrOne = random.randrange(0,2)

    # If we get a zero, we say that was a heads
    # If we get a one, we say that was a tails

    if zeroOrOne ==0:
        nTails = nTails + 1
    else:
        nHeads = nHeads +1
    nFlips = nFlips + 1

print()
print('Out of',nFlips,'coin tosses we had:',nHeads,'heads and',nTails,'tails.')
