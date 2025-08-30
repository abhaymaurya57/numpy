# array indexing is the same as acessing an array element 
#start with 0

import numpy as np

a=np.array([1,2,3,4,5])
print(a[1])
print(a[-1])
print(a[1:4])
print(a[-2:-1])
print(a[-4:-1])
print(a[-1:-8:-2])

print(a[3] + a[4]+a[1])
print(a[0:3],a[2:5])

#    2D arrays
b=np.array([[1,2,3,4,5],[6,7,8,9,10]],ndmin=5)
print(b.ndim)
print('2nd element in the 1st row   ',b[0][0][0][0][1])
print('4nd element in the 2st row   ',b[0][0][0][1][3]) 

# 3D array
c=np.array([[[1,2,3,4],[3,4,5,6],[6,7,8,9]],
            [[1,2,3,4],[3,4,5,6],[6,7,8,9]]])
print(c[1][1][1])

print(c.ndim)