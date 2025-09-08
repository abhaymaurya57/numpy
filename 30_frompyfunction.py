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

# cheking if  this function in ufunc or net:

print(type(np.add))

# concatenate()
print(type(np.concatenate))

#what if ufunc does not exist:

'''  print(type(np.kuxx_bhi))  '''  # error nahi show karta hai par execute time pe error dega

# use an if statment check if the function a ufunc or not
if type(np.add)==np.ufunc:
    print('yes this function is u function')
else:
    print('this function is not ufunc ')
