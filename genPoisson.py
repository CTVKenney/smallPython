#!/usr/bin/env python3

from decimal import *
import math
import sys
import random
from datetime import datetime

random.seed(datetime.now())

if len(sys.argv) > 1:
    commandLineLam = float(sys.argv[1])
else:
    commandLineLam=1

#A biased coinflip: returns 1 with probability p, 0 with probability 1-p
def flip(p):
    if random.random() < p:
        return 1
    else:
        return 0

#Outputs the value of the partial sum of the power series
#for e^lam over the summand interval from start (inclusive) to stop-1 (inclusive)
def eSeriesRange(lam, stop, start = 0):
    return sum([lam**i / math.factorial(i) for i in range(start, stop)])

#Inputs a list of positive numbers corresponding to wieghts on 0,1,...,len(list)-1;
#Outputs a random number 0,1,...,len(list)-1 with probability proportional to its weight.
def weightDie(weightList):
    totWeight = sum(weightList)
    randDraw = random.random()*totWeight
    spot = 0
    distance = 0
    for w in weightList:
        distance = distance+w
        if randDraw <= distance:
            break
        spot = spot +1
    return spot

#Two approaches for sampling from a Poisson distribution:
#(1) Using the Rare Event Binomial Approximation:
#If n*p_n -> lam as n -> infty, then the binomial distributions Bin(n, p_n)
#converge pointwise to Pois(lam).

#(2) A "Binary Search" with Coinflips over the Natural Numbers

def main(lam = commandLineLam):
    #First, we use a pseudo binary search to find an interval of length 2^n which contains our draw
    drawn = flip(math.exp(-lam))
    if drawn:
        return 0
    upperN = 1
    while not drawn:
        prob = (math.exp(-lam) * eSeriesRange(lam, 2**upperN, 2**(upperN -1)))/(1 - math.exp(-lam) * (eSeriesRange(lam, 2**upperN))) #The probability,
        #Conditional on X>2^(upperN-1)-1, that X<=2^upperN.
        drawn = flip(prob)
        upperN = upperN+1-drawn
    #It should now be the case that drawn=1 and upperN is a power such that our Poisson r.v. X lies between 2^(upperN-1) and 2^upperN -1, inclusive.
    withinDyad = weightDie([lam**k/math.factorial(k) for k in range(2**(upperN-1),2**upperN)])
    finalDraw = 2**(upperN-1) + withinDyad
    return finalDraw

if __name__ == '__main__':
    main()
