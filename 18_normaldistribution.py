# normal(Gaussian) distribution - very important.
# random.normal() method-loc(mean),scale(standard distribution),size

# we are generating a normal distribution of size 2*3
from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

a = random.normal(size=(2,3))
print(a)

#here we will generate a random dist of size 2*3 with mean(loc) at 1 and standard deviation of 2:
b = random.normal(loc=1,scale=2,size=(2,3))
print(b)

# visualization of normal distribution 
sns.distplot(random.normal(size=1000),hist=False)
plt.show()

# the curve of a normal dist is also called as bell curve