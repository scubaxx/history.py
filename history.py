#!/usr/bin/env python

# import bitcoin
from bitcoin import *

#View address transaction history
a_valid_bitcoin_address = '1DFRgZCaeXPjCuD3QUR53FGgV2LDo6TTZe'
print(history(a_valid_bitcoin_address))
