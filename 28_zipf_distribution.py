# zify dist: Its defination is like.. common word in english has occurs nearly 1/5 time as of the mosthindi words.

#param - a(dist param),size
#semple for zipf s=dist with a as 2 with size 2*3
from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
a = random.zipf(a=2,size=(2,3))
print(a)

# visualization of zify dist
a = random.zipf(a=2,size=1000)
sns.distplot(a[a<10],kde=False)
plt.show()