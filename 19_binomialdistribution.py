# binomial dist - discrete dist - binary output.
# param - n(number of trials) ,p(probability),size(shape -returned array)

#given 10 trial for a coin which will generated 10 data points:

from numpy  import random
a = random.binomial(n=10,p=0.5,size=10)
print(a)

# visualization 