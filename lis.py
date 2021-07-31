#!/usr/bin/env python3

import sys
import random

def lis(L):
    """ 
    Inputs a list L of DISTINCT comparable elements.
    Outputs the length of the longest increasing subsequence in L.
    """
    if len(L) == 0:
        return 0
    minIndex = L.index(min(L))
    leftL = L[:minIndex]
    rightL = L[minIndex+1:]
    return max(lis(leftL), lis(rightL)+1)

def lds(L):
    """
    Inputs a list L of DISTINCT comparable elements.
    Outputs the length of the longest decreasing subsequence in L.
    """
    if len(L) == 0:
        return 0
    maxIndex = L.index(max(L))
    leftL = L[:maxIndex]
    rightL = L[maxIndex+1:]
    return max(lds(leftL), lds(rightL)+1)
    
def randperm(n):
    """
    Inputs a positive integer n
    Outputs a random permutation of the elements 0,1,...,n-1
    """
    unshuffled = list(range(n))
    shuffled = []
    while len(unshuffled) > 0:
        element = random.choice(unshuffled)
        shuffled.append(element)
        unshuffled.remove(element)
    return shuffled

def main(n):
    shuf = randperm(n)
    return lis(shuf), lds(shuf)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Usage: enter a positive integer in the command line')
    else:
        print(main(int(sys.argv[1])))
