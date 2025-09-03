# data distribution is a list of all possible value and how often each value occor.
# sach list are important when working with statics and data science

# random distribution : probability function ,

# now we will generate 1 -D with 100 valuews where every value has to be 3,5,7,9

#the probabily for the value 3 is set to be 0.1
#the probabily for the value 5 is set to be 0.3
#the probabily for the value 7 is set to be 0.6
#the probabily for the value 9 is set to be 0
# the sum of all probality numbers should be 1

from numpy import random
a = random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=(100))
print(a)

# Now we will return 2-D with 3 rows each containing 5 values.
b = random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=(3,5))
print(b)