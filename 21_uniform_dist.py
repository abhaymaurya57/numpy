# uniform dist - it is onlt made for probability(p)
#param - a(lower bound - 0.0),b(upper bound - 1.0), size()

from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 
# a = random.uniform(low=0.2,high=.8,size=(2,3))
a = random.uniform(size=(2,3))
print(a)

#visualization of uniform dist
b=sns.distplot(random.uniform(size=1000),hist=False)
plt.show()