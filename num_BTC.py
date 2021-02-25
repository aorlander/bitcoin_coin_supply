import os
import math
import shutil
from pathlib import Path

# Input is block height (integer)
# Return total number of tokens that have been mined so far (up to and including the given block)
def num_BTC(b):
    reward = 50
    tok = 0
    height = 1
    max = 210000

    while height <= b :
        height = height + 1
        tok = tok + reward
        tok_int = int(tok)
        remainder = pow(tok_int, 1, max)
        if remainder == 0:   # Reward halves every 210k blocks
            reward = reward/2 
            
    print(float(tok))
    return float(tok)

# test cases
# num_BTC(1)
# num_BTC(2)
# num_BTC(4199)
# num_BTC(4200) # split 
# num_BTC(4201)