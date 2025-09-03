#sort()-the numpy ndarray object has a function which 
#is called sort(),and this will sort a specified aray,

import numpy as np
a = np.array([3,2,1,0])
print(np.sort(a))   # this methos like a copy()

# sort the array alphatically
b = np.array(['banana','cherry','apple'])
print(np.sort(b))

# sort the boolean array:
c = np.array([True,False,True])
print(np.sort(c))

#sort the 2-D array
d = np.array([[3,2,4],[5,0,1]])
print(np.sort(d))

# both array join and sort and again 2-d array
d = np.array([[3,2,4],[5,0,1]])
dd=d.view()
print('dd',dd)
e = dd.reshape(-1)
f=np.sort(e)
print(f.reshape(2,3))