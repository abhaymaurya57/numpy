# getting some element out of an existing array and 
#creating a new array is called filtering.

# A boolean index list is a list of boolean corresponding
# to indexes in the array.(True and False)

#creating an array from the element on index 0 to 12:
import numpy as np

a = np.array([41,42,43,44])
b=[True,False,True,False]
ab=a[b]
print(ab)     #[41 43]

# Now we will create a filter array
# that will return only values higher than 42.
c = np.array([55,41,42,43,44])
empty = []
for element in c:
    if element > 42:
        empty.append(True)
    else:
        empty.append(False)
d = c[empty]
print(empty)
print(d)

# creating a filter array that will return only even
#element from the original array.
e = np.array([1,2,3,4,5,6,7])
empty1=[]
for i in e:
    if i%2==0:
        empty1.append(True)
    else:
        empty1.append(False)
f = e[empty1]
print(empty1)
print(f)

# yes you can also create filter directly from aaray
g = np.array([41,42,43,44])
empty2= g > 42
print(empty2)
h = g[empty2]
print(h)

#******************

e = np.array([1,2,3,4,5,6,7,8])
empty1 = e%2==0
f = e[empty1]
print(empty1)
print(f)