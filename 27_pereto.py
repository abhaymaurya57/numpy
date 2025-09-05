# pereto Dist: 80:20 ratio.(20% factors cause 805 cause autcomen or result)

# param-a(shape param),size
#sample for pareto dist with shape 2 with size 2*3
from numpy import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

a = random.pareto(a=2,size=(2,3))
print(a)

# visualization 
sns.distplot(random.pareto(a=2,size=1000),kde=False)
plt.show()