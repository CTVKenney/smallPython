#!/usr/bin/env python3

from random import randrange
import networkx as nx

def randSubs(S,k):
    """ Inputs a set S and a nonnegative integer k.
    Outputs a random subset of S of size k, if possible.
    Throws an error if k > #S.
    """
    n = len(S)
    if k > n:
        raise Exception('randSubs requires the size k of the random subset to be smaller than the cardinality of the universe S')
    subs = set()
    for j in range(k):
        elInd = random.randrange(len(S))
        s = S[elInd]
        subs = subs.union({s})
        S = S.difference({s})
    return subs

def ists(x,n,k):
    """Inputs nonnegative integers x,n,k with k <= n.
    Outputs a list of sets of length x. 
    All sets are of size k within {0,1,...,n-1}.
    """
    universe = set(range(n))
    return [randSubs(universe, k) for i in range(x)]

def main():
    pass

if __name__ == '__main__':
    main()
