# shape of an array - the shape of an array is the number of element in each dimention

# now we will try to get the shape of any array

import numpy as np
a = np.array([[1,2,3,4],[5,6,7,8]])
print(a.shape)    # (2,4)

# (2,4) whicj means the array has 2 dimention  and 
# it has 4 element

#now will create a 5-d array using ndmin
b = np.array([1,2,3,4,5],ndmin=5)
print(b)        # [[[[[1 2 3 4 5]]]]]
print(b.shape)  # (1, 1, 1, 1, 5)