#!/usr/bin/env python3

#Takes in a number of bits and outputs a random dyadic rational with denominator
#2^numBits. This is an approximation to a uniform[0,1], and the approximation gets
#better for numBits larger.

import random
import math
from datetime import datetime
random.seed(datetime.now())

numBits = 15 #A parameter that can be altered,
#which determines how good the approximation to normal will be.

def main():
    randList = [random.randrange(2) for i in range(numBits)]
    toBits = [randList[i]*(0.5 ** (i+1)) for i in range(numBits)]
    randUniform = sum(toBits)
    print(randUniform)
    return

if __name__ == '__main__':
    main()
