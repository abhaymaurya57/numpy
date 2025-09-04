# Multinomial dist: it is a generalization of binomial dist.
# parameter - n (number of posibility or outcome),pvals(list of possibility or outcome),size(shape of return array)
# draw out sample for dice roll

from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

a = random.multinomial(n=6,pvals=[1/6,1/6,1/6,1/6,1/6,1/6])
print(a)

# multinomial sample will not produce a single value , they will produce one value for each pvals.
sns.distplot(random.multinomial(n=6,pvals=[1/6,1/6,1/6,1/6,1/6,1/6])
,hist=False)
plt.show()