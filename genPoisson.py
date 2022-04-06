#!/usr/bin/env python3

from decimal import *
import math
import sys
import random
from datetime import datetime

random.seed(datetime.now())

#A biased coinflip: returns 1 with probability p, 0 with probability 1-p
def flip(p):
    if random.random() < p:
        return 1
    else:
        return 0

#Outputs the value of the partial sum of the power series
#for e^lam over the summand interval from start (inclusive) to stop-1 (inclusive)
def eSeriesRange(lam, start, stop):
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

def binSearchPoisson(lam):
    #First, we use a pseudo binary search to find an interval of length 2^n which contains our draw
    drawn = flip(math.exp(-lam))
    if drawn:
        return 0
    upperN = 1 #upperN is the exponent of 2 at the upper end of the next range of length power-of-2
    while not drawn:
        prob = eSeriesRange(lam, 2**(upperN-1), 2**upperN)/(math.exp(lam) - eSeriesRange(lam, 0, 2**(upperN-1))) #The probability,
        #Conditional on X>2^(upperN-1)-1, that X < 2^upperN.
        drawn = flip(prob)
        upperN = upperN+1-drawn
    #It should now be the case that drawn=1 and upperN is a power such that our Poisson r.v. X lies between 2^(upperN-1) and 2^upperN -1, inclusive.
    withinDyad = weightDie([lam**k/math.factorial(k) for k in range(2**(upperN-1),2**upperN)])
    finalDraw = 2**(upperN-1) + withinDyad
    return finalDraw

rareTries = 100

def rarEventPoisson(lam):
    prob = lam/rareTries
    return sum([flip(prob) for i in range(rareTries)])
