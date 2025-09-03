#you can search array for a certain value
# and return the indexs that get the match by using wehre()
import numpy as np
a=np.array([1,2,3,4,5,6,4,4])
print(a.dtype)
b=np.where(a==4)
print(b)     #(array([3, 6, 7]),)

#Now will find he indexes where the values are even:
c=np.array([1,2,3,4,5,6,7,8])
d=np.where(c%2==0)
print(d)

#Now will find he indexes where the values are odd:
c=np.array([1,2,3,4,5,6,7,8])
d=np.where(c%2==1)
print(d)

#search sorted-perform binary search in array. 
#find will now the index where the value 7 shuld be insterted.
import numpy as np
e = np.array([6,7,8,9])
f=np.searchsorted(e,7)
print(f)

#now we will sear from right side
g=np.searchsorted(e,7,side='right')
print(g)

# how to search multiple values:
h=np.array([1,3,5,7])
i=np.searchsorted(h,[2,4,6])
print(i)