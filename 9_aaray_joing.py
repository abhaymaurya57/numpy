#join the numpy array-
# here for this we will pass concatenate()

import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])
c=np.concatenate([a,b])
print("concatenate\n",c)
print(np.ndim(c))

# join of 2-D arrays along with rows(axis -1)
d = np.array([[1,2],[3,4]])
e = np.array([[5,6],[7,8]])
f=np.concatenate([d,e],axis=1)
print("concatenate with axis\n",f)

#joing array using the stack function:g
g = np.array([1,2,3])
h = np.array([4,5,6])
i=np.stack([g,h],axis=1)
print("stack\n",i)

#stacking along with rows: hstack()
j = np.array([1,2,3])
k = np.array([4,5,6])
l=np.hstack([j,k])
print("htack\n",l)

#stacking along with column
m = np.array([1,2,3])
n = np.array([4,5,6])
o=np.vstack([m,n])
print("vstack\n",o)
print(np.ndim(o))

#stacking along with height(depth)
p= np.array([1,2,3])
q = np.array([4,5,6])
r=np.dstack([p,q])
print("dstack\n",r)
print(np.ndim(r))