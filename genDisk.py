#!/usr/bin/env python3

import genUniform
import math

#This function outputs a uniformly random point in the unit disk (the set of vectors in R^2 with norm at most 1).
#It takes as input two uniform random draws from [0,1].

def main():
    a = genUniform.main()
    b = genUniform.main() #Two uniformly random elements of [0,1].
    angle = (math.tau)*a
    radius = math.sqrt(b)
    return (radius*math.cos(angle), radius*math.sin(angle))

if __name__ == '__main__':
    main()
