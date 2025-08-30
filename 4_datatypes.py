'''  data type in python: string ,int,flot,boolen,complex  '''
# data type in numpy 

# i for integer
# b for boolean
# u for unsigned integer
# f for float
# c fot complex float
# m for timedelta
# M for datetime
# O for object
# S for string
# U for unicode string
# v - memory 

#checking the data type of nupy of array-dtype

import numpy as np

a = np.array([1,2,3,4])
print(a.dtype)   #->  int64

#checking the data type of string

b = np.array(['apple','bananna','cherry'])
print(b.dtype)   #   <U7

# creating aray with a defined data type
c = np.array([1,2,3,4],dtype='S')
print(c)         #  [b'1' b'2' b'3' b'4']
print(c.dtype)   #  |S1

#now we will create an array with data type of 4 byte int:
d = np.array([1,2,3,4],dtype='i4')
print(d)         #    [1 2 3 4]
print(d.dtype)   #    int32

'''if a type is given in which the element cannot be
casted then numpy will raise error. what if a value
cannot be converted
'''
d = np.array(['2','3'],dtype='i')
print(d)         #    [2 3]
print(d.dtype)   #    int32

#error
# d = np.array(['a','2','3'],dtype='i')
# print(d)        
# print(d.dtype) 

#converting data type on existing array- astype()
import numpy as np
e= np.array([1.1,2.1,3.1,4.1])
print(e)
print(type(e.dtype))
f=e.astype('i')
# f=e.astype(int)
print(f)
print(type(f.dtype))

#converting data type from integer to boolean
import numpy as np
g= np.array([1,0,3])
print(g)
print(type(g.dtype))
# h=e.astype('b')
h=g.astype(bool)
print(h)
print(h.dtype)