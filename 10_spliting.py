#spliting in numpy-It is revers to joing,breaking the array
#array_split()

#split the array 3 parth:
import numpy as np

a = np.array([1,2,3,4,5,6])
b=np.array_split(a,3)
print(b)     #[array([1, 2]), array([3, 4]), array([5, 6])]

# now we will split this aray in 4 parth
c=np.array_split(a,4)
print(c)   #[array([1, 2]), array([3, 4]), array([5]), array([6])]

#split into array with index
d=np.array([1,2,3,4,5,6])
e=np.array_split(d,3)
print(e[0])   #[1 2]
print(e[1])   #[3 4]
print(e[2])   #[5 6]

#splitting the 2-D array
f=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
g=np.array_split(f,3)
print(g)

#split 2-D array into three 2-D aray
h=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
i=np.array_split(h,3)
print(i)

#spliting the 2-D into three 2-D alongs with rows
j=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
k=np.array_split(j,3,axis=1)
print(k)

# alternate solution is using the hsplit(),opposite hstack()
l=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
m=np.hsplit(l,3)
print(m)