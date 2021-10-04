#!/usr/bin/env python3

import random
import math

numDraws = 10000 #A parameter that can be altered,
#which determines how good the approximation to normal will be.

def main():
    randList = [random.randrange(2) for i in range(numDraws)]
    print(2*(sum(randList) - numDraws/2)/(math.sqrt(numDraws)))
    return

if __name__ == '__main__':
    main()
