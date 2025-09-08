# Arithmati operation: +,-,/,*

# By using ufunc addition argument like , where ,dtype and out.
# here noe we will use add()

import numpy as np
a = np.array([10,11,12,13,14,15])
b = np.array([20,21,22,23,24,25])
c = np.add(a,b)
print(c)

# substract the value 
a = np.array([10,11,12,13,14,15])
b = np.array([20,21,22,23,24,25])
d = np.subtract(a,b)
print(d)

# multiply the value
a = np.array([10,11,12,13,14,15])
b = np.array([20,21,22,23,24,25])
e = np.multiply(a,b)
print(e)

# power() function raise the value from the 1st array 
# to the power of the value of 2nd array and return the result in a new array.
a = np.array([10,11,12,13,14,15])
b = np.array([2,3,4,5,6,7])
f = np.power(a,b)
print(f)

# reminder - mod() and reminder() function return the
#  reminder of the 1St array corrosponding to the 2nd array,and result in the new array.
a = np.array([10,11,12,13,14,15])
b = np.array([2,3,4,5,6,7])
g = np.mod(a,b)
print(g)

g = np.remainder(a,b)
print(g)

#quotient and mod(reminder)
# the divmod() function return both the quotient and mod.
a = np.array([10,11,12,13,14,15])
b = np.array([2,3,4,5,6,7])
h = np.divmod(a,b)
print(h)

# absalute() and abs() - do the same operation but here we should use absolute() to avoid confusion with python inbuilt function math.abs()

a=np.array([-1,-2,-3,-4,-5])
b = np.absolute(a)
print(b)