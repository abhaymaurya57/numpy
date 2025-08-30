# diffrence b/w numpy array copy and view

# we will mak e a copy ,change in original array ,a nd display both

import numpy as np
a = np.array([1,2,3,4,5])
b=a.copy()
print(a)
print(b)
b[0]=42
print(a)
print(b)


# now we will make a view,change original ,display
c = np.array([1,2,3,4,5])
d=c.view()
print(c)
print(d)
c[0]=42
print(c)
print(d)
d[0]=100
print(c)
print(d)