'''now we will create a numpy ndarray object
    the array object in numpy is called nd array
    array()
'''
import numpy as np

x=np.array([1,2,3,4,5,])
# print(x)
# print(type(x))

'''we can also pass a list ,tuple or any array 
like object with array().and it will be coverted to ndarray'''
y=np.array((1,2,3,4,5))
# print(y)
# print(type(y))

#dimension in array-a dimension in array in one level of array depth (nested aray)

# 0-D arrays - scaler,are the element in an array,each value in array is a zero d(0-d)
# Now will create -_d array with value 42

a = np.array(42)
# print(a)         # 0-d
# print(type(a))

# 1-d array - an array that has o-d arrays as its elemnt is called unidirectional or 1-d
b=np.array([1,2,3,4,5])
# print(b)

# create a 2D array containg 2 Array with certain values.

c=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(c)

# Now will will create a 3-D array with 2-D array.

d=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])
# print(d)

# check how many dimention the array have:  ndim attribute

e=np.array(42)
f=np.array([1,2,3,4,5])
g=np.array([[1,2,3,4,5],[6,7,8,9,10]])
h=np.array([[[1,2,0],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])
print(e.ndim)
print(f.ndim)
print(g.ndim)
print(h.ndim)

# create an array with 5 dimention and varify that its has 5 direction 
i=np.array([1,2,3,4,5],ndmin=5)
print(i)
print('number of dimention',i.ndim)