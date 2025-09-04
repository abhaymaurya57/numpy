# logistic dist - describe growth it is basically imp in regration and neural network 
# param - loc(mean-0.0),scale(standard deviationn , 1),size

# draw 2*2 sample of logistic with mean at 1 and stddev 2.0 

from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

a = random.logistic(loc=1,scale = 2,size=(2,3))
print(a)

# visualization of logistic dist
sns.distplot(random.logistic(size=1000),hist=False)
plt.show()