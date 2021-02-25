import os
import math
import shutil
from pathlib import Path

# Input is block height (integer)
# Return total number of tokens that have been mined so far (up to and including the given block)
def num_BTC(b):
    reward = 50.00
    tok = 0.00
    mined = 0

    while mined < b :
        mined = mined + 1
        tok = tok + reward
        if pow(mined, 1, 210000) == 0:   # Reward halves every 210k blocks
            reward = reward/2 

    return float(tok)