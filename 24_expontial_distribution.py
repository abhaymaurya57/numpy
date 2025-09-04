# expontil dist: it is use for describing the till next event that is like faiure or success.
#param - scale(inverse of rate(see lam poisson dist)),size

# here we will dwar a sample for expontial dist with 2.0 scale and 2*3 size.

from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

a = random.exponential(scale=2,size=(2,3))
print(a)

sns.distplot(random.exponential(scale=2,size=(2,3)),hist=False)
plt.show()