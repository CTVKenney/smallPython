#!/usr/bin/env python3

import math
import random
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
        listForm = [el for el in S]
        elInd = random.randrange(len(S))
        s = listForm[elInd]
        subs = subs.union({s})
        S = S - {s}
    return subs

def iterColors(F,X,Y,x,y,m,n,k):
    """
    Inputs a subset F of X times Y, x an element of X and y an element of Y.
    For i=0..m-1, we will choose new color lists from X, then Y, then X, and so on.
    Each new color list must be compatible with the last-chosen color list. [What if it becomes impossible? This will not happen except possibly at the first draw.]
    k is the length of the lists.
    n is the size of the full color set, say {0,1,...,n-1}
    """
    G = nx.Graph()
    G.add_nodes_from(X)
    G.add_nodes_from(Y)
    G.add_edges_from(F)

    Gamma = set(range(n))

    #Each iteration will produce a dictionary {vertex: list, vertex':list',...} for vertices in X (even iterations)
    #or Y (odd iterations).

    firstColDict = {}

    for v in X:
        firstColDict[v] = randSubs(Gamma,k)

    colorIters = [firstColDict]

    for i in range(1,m):
        if i % 2 == 0:
            nextColorDict = {}
            for v in X:
                S = Gamma
                for w in G[v]:
                    S = S - colorIters[i-1][w]
                nextColorDict[v] = randSubs(S,k)
            colorIters.append(nextColorDict)
        else:
            nextColorDict = {}
            for v in Y:
                S = Gamma
                for w in G[v]:
                    S = S - colorIters[i-1][w]
                nextColorDict[v] = randSubs(S,k)
            colorIters.append(nextColorDict)
    
    equalList = [bool(colorIters[i][x] & colorIters[i+1][y]) for i in range(0,m-1,2)]

    return sum(equalList)/(math.floor(m/2))


def main():
    pass

if __name__ == '__main__':
    main()
