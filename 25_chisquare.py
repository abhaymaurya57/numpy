# chi square Dist: it is basically used as a basis to verify  the Hypothesis:
#param : df (degree of freedom),size

#sample for chi squred dist with of 2 with size 2*3
from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

a = random.chisquare(df=2,size=(2,3))
print(a)

# visualization of chi square.
sns.distplot(random.chisquare(df=2,size=100),hist=False)
plt.show()