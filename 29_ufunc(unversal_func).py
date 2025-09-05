#ufunc- stands for universal function and they are acually numpy function that operaters on the ndarray objects.
# ufunc also takes additional arguments like ,whre,dtype and out.
# vectorization - convating the iterative statement into a vector based statment
# example with out ufunct here we will use python in built Zip().

from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = [1,2,3,4]
y = [4,5,6,7]
z=[]
for i ,j in zip(x,y):
    z.append(i+j)
print(z)

# with ufunction we will now add() function 
x = [1,2,3,4]
y = [4,5,6,7]
z=np.add(x,y)
print(z)