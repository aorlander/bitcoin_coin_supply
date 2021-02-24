import os
import math
import shutil
from pathlib import Path

# Input is block height (integer)
# Return total number of tokens that have been mined so far (up to and including the given block)
def num_BTC(b):
    r = 50
    n = 0
    count = 0

    while count < b :
        count = count + 1
        n = n + r
        i = int(n)
        if pow(i, 1, 210000) == 0:   # Reward halves every 210k blocks
            r = r/2 
            
    print(float(n))
    return float(n)

# test cases
num_BTC(1)
num_BTC(2)
num_BTC(4199)
num_BTC(4200) # split 
num_BTC(4201)