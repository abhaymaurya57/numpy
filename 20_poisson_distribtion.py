# poisson distribution - it estimates how many time an event can happen.
# parameter - lam(number of occurance or rate) , size
# generate a random 1*10 dist for the occurance 2
import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

a = random.poisson(lam=2,size=10)
print(a)

# visualization of poisson dist
sns.distplot(random.poisson(lam=2,size=1000),kde=False)
plt.show()

# presenting both the plots in same figure normal and poisson dist.
sns.distplot(random.normal(loc=50,scale=7,size=1000),hist=False,label='Normal')
sns.distplot(random.poisson(lam=50,size=1000),hist=False,label='Poisson')
plt.show()  


#n*p== lam
