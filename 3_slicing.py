#slicing array - slicing in python means taking element fron q given index to aother index
#[start:end]  ,   [start:end:step]

#now we will slice an element from 1 to 5
import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9])
print(len(a))
print(a[0:4])
print(a[0:8:1])
print(a[0:8:2])
print(a[-1:-8:1])
print(a[-1:-8:-1])
print(a[-1:-8:-2])
print(a[::2])
print(a[::-2])

#slicing 2-D array 
b=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(b[1][0:5:2])