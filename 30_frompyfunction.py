# to create your own ufunc, you have to define a function,
#like you do in normal functon in python,then you add it 
# to the numpy function with frompyfunc() methos.

# argument of frompyfunction(): function,input,output

# create your own for addition:
import numpy as np
def myadd(x,y):
    return x+y

myadd = np.frompyfunc(myadd,2,1)  # 2 array, output 1
print(myadd([1,2,3,4],[5,6,7,8]))
 