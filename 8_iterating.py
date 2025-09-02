# iterating Array - means going though the element
#  one by one or step by step . like For loop
def star():
    print(35*'*')
# Iterate the element of 1-D
import numpy as np
a = np.array([1,2,3])
star()
for i in a:
    print(i)

# Iterate 2-D
b = np.array([[1,2,3],[4,5,6]])
star()
for i in b:
    print(i)

#Iterate on each scalar element of the 2-D
c = np.array([[1,2,3],[4,5,6]])
star()
for i in c:
    for a in i:
        print(a)

# iterrate on 3-D
c = np.array([[[1,2,3],[4,5,6]]])
star()
for i in c:
    for a in i:
        for b in a:
            print(b)

#Iterating arrays using the nditer() function.
# Now we will Iterate on each scaler element

d = np.array([[[1,2],[3,4],[5,6],[7,8]]])
star()
for i in np.nditer(d):
    print(i)

e=([[['a','b'],['c','d'],['e','f'],[7,8]]])
star()
for i in np.nditer(e):
    print(i)

#now we will Iterate with diffrent step sizes.
f=np.array([['a','b','c','d'],['e','f',7,8]])
star()
for i in np.nditer(f[:,::2]):
    print(i)
