# binomial dist - discrete dist - binary output.
# param - n(number of trials) ,p(probability),size(shape -returned array)

#given 10 trial for a coin which will generated 10 data points:
import matplotlib.pyplot as plt
import seaborn as sns
from numpy  import random
a = random.binomial(n=10,p=0.5,size=10)
# print(a)

# visualization of binomial dist:

sns.distplot(random.binomial(n=10,p=0.5,size=1000),hist=True,kde=False)
plt.show()

#difference b/w normal and binomial - normal(contunues) and binomial (discreate)
# i use 500 data poin t for binmial and under 100 data point for nor

sns.distplot(random.normal(loc=50,scale=5,size=1000),hist=False,label='Normal')
sns.distplot(random.binomial(n=10,p=0.5,size=1000),hist=False,label='Binomial')
plt.show()