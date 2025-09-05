#rayleight list: it is use in signal processing.
#param - scale(standard deviation , how flat the distribution is .. default 1.0 ),size

# sample for R1 with scale of 2.0 with size of 2*3
from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

a = random.rayleigh(scale=2,size=(2,3))
print(a)

#visualization of rayleigh dist
sns.distplot(random.rayleigh(scale=2,size=1000),hist=False)
plt.show()