# Random Meaning - something that cannot be predicted logically.

#Now we will generate a random number from 0 to 100
import numpy as np
from numpy import random
a = random.randint(100)
print(a)

# you can also generate float() via rand()
b = random.rand()
print(b)

# you can also generate random Array.
# we will generate a 1-D array containing 5 random int from 0 to 100:

# c = random.randint(100,size=10)
c = random.randint(100,size=(100))
print(c)
print()

#2-D array with 3 row , each row 5 random int from 0 to 100
d = random.randint(100,size=(3,5))
print(d)

# float 
d = random.rand(100)
print(d)

# 2-D array with 3 rows ,each containig 5 random float
e = random.rand(3,5)
print(e)

# you can also generate random number from an array
# choice()
f = random.choice([1,2,3,4,5,6])
print(f)

# 2-D array choice
# g = random.choice([1,2,3,4,5,6],size=(3,5))
g = random.choice([0,1],size=(3,5))
print(g)

f = random.choice([[1,2,3],[4,5,6]])
print(f)
