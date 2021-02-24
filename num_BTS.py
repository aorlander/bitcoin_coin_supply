import math
import os

# Input is block height (integer)
# Return total number of tokens that have been mined so far (up to and including the given block)
def num_BTC(b):
    max = 210000
    r = 50
    n = 0
    count = 0

    while count <= b :
        n = n + r
        i = int(n)
        if pow(i, 1, max) == 0:   # Reward halves every 210k blocks
            r = r/2 
        count = count + 1
    
    c = float(n)
    print(c)
    return c

num_BTC(1)
num_BTC(2)
num_BTC(4199)
num_BTC(4200)
num_BTC(4201)