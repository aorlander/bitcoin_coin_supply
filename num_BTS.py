import math

# Return total number of tokens that have been mined so far (up to and including the given block)
# Bitcoin tokens are generated through block rewards. 
# Initially, the block reward was 50 BTC, and the reward halves every 210,000 blocks. 
# Thus at Block 1 there were 50 BTC in circulation. At Block 2, there were 100 BTC etc.

def num_BTC(b):
    max = 210000
    r = 50
    n = 0
    count = 0

    while count < b:
        n = n + r
        i = int(n)
        split = pow(i, 1, max)
        if split == 0: # reward halves every 210k blocks
            r = r/2 
        count = count + 1
    
    c = float(n)
    return c


blockHeight = 14055
num_BTC(blockHeight)