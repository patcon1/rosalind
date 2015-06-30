
# 24 june i completed this, it took me ages. I struggled out of all proportion with its difficulty
# i need much more practice


__author__ = 'pconn'

import math

# mendelian problem, independent assortment
# generation zero is an Aa Bb individual. every generation gives rise to 2 offspring
#both are mated with Aa Bb to give 2 offspring

# Problem: the probability at least N Aa Bb will be in the Kth generation

#1. determine The number in the generation

k = int(input('how many generations?'))
pop = 2 ** k

n = int(input("at least "))

#pop = int(input('from how large a population'))


# the probability of an Aa when mated with an Aa is 0.5
# the probability of an Aa when mated with the offspring of this union is also 0.5
#  1/4 AA, 1/2 Aa, 1/4 aa mated with Aa returns back to these proportions
# According to the independence the number of Aa Bb will just be Aa* Bb = 0.25

# if there are k^2 individuals in generation K

# sum up the binomial probabilities of the event

# the probability of it happening N times
# (population factorial / n factorial) * Probability^population * 1-probability)^(pop-n)
# sum this all the way up to n


# to get at least n go from zero to one les than N adding up all the probabilities
# then subtract that from 1


probability = 0

for i in range(0,n):
    # this calculates the probability of exactly i
    specprob = math.factorial(pop) / (math.factorial(i) * math.factorial(pop-i))
    print (specprob)
    specprob *= (0.25 ** i) * (0.75 ** (pop-i))

    print(specprob)
    # add the probability on
    probability += specprob

print( 1-probability )
