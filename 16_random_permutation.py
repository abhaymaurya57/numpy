#permutation refers to an arangement of element like [3,2,1] is permutation of [1,2,3] and vice virsa
# the numpy random module provides 2 methods :shuffle() and permutation()

# now we will random suffle element foe the below arrat:

#*** shuffle() method make change to the original array
from numpy import random
import numpy as np
a = np.array([1,2,3,4,5])
random.shuffle(a)
print(a)

# now we will generate  a permutation of element for the below array:
# the permutation method leaves the original array unchange
b = np.array([1,2,3,4,5])
c=random.permutation(b)    # not change original array
print(b)
print(c)