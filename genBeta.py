#!/usr/bin/env python3

"""
The Beta distribution has parameters alpha and beta, known as the prior sample sizes.
We'll try to implement a rejection sampling approach.
As with many of these programs, I have not yet taken the time to think about
numerical stability issues/how the computer is holding the numbers in memory,
instead treating them as idealized numbers.
"""

import genUniform as gU

def main(alpha, beta):
    success = 0
    while success == 0:
        (x,y) = (gU.main(), gU.main())
        if y <= (x**(alpha -1))*((1-x)**(beta - 1)):
            res = x
            success = 1
    print(res)
    return res

if __name__ == '__main__':
    main(1,1)
