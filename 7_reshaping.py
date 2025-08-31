# reshaping - means changing the shape of
#  an array , like adding or removing the element

# reshaping from 1-D to 2-D
import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
b= a.reshape(4,3)
print(a)  #[ 1  2  3  4  5  6  7  8  9 10 11 12]
print(b)
'''
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]
'''

# reshaping from 1-D to 3-D
import numpy as np
c = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
d= c.reshape(2,3,2)
print(c)  #[ 1  2  3  4  5  6  7  8  9 10 11 12]
print(d)
'''[[[ 1  2]
  [ 3  4]
  [ 5  6]]

 [[ 7  8]
  [ 9 10]
  [11 12]]]'''


# return copy or view
e=np.array([1,2,3,4,5,6,7,8])
f=e.reshape(2,4).base
print(f)


g=e.copy()
g[0]=100
h=g.reshape(4,2).base
print(h)

# unknown dimention - you are only allow to have one
# unknown dimention. pass -1

i= np.array([1,2,3,4,5,6,7,8,9,9,9,9,2,2,2,2])
j=i.reshape(2,2,-1)
print(j)

# flating the array by converting multidimentional array in 1-D
k=np.array([[1,2,3],[4,5,6]])
l=k.reshape(-1)
print(l)

# there are alot of function for changing the shapes of an array in numpy.
#like flatten , ravel and also rearrangeing the element rot90,flip,fliplr,flipud.
# they all are actually comes under advance numpy
