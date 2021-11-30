#!/usr/bin/env python3

import math

"""
My attempt to implement a heap using python lists
The lists should consist of things which can be compared.
Normally, these are integers and we compare using the usual ordering on Z

The elements of the python list of length n (with indices 0,1,...,n-1) are thought of as being
in an 'almost complete' oriented binary tree, where the root of the tree corresponds to index 0,
the left child of the root <-> index 1, the right child of the root <-> index 2, and so on.
In general, the parent of the element at index i is at floor((i-1)/2).
"""

#Also known as find-max, peek simply returns the max element of a max heap.
#Since it's a max heap, this is very simple.
def hPeek(H):
    return H[0]

#H is currently a max heap.
#newEl is a new element we want to add
def hInsert(newEl, H):
    newList = H + [newEl] #Initially, newEl is added as a child of the first node with an available child spot.
    newPos = len(H) # = len(newList) -1, the position of newEl
    print(newList, newPos)
    while (newPos > 0):
        if newList[newPos] > newList[math.floor((newPos - 1)/2)]:
            newList[newPos] = newList[math.floor((newPos - 1)/2)]
            newList[math.floor((newPos - 1)/2)] = newEl
            newPos = math.floor((newPos - 1)/2)
        else:
            newPos = 0
    return newList

def hPop(H):
    alpha = H[0]
    newList = H[:-1]
    newList[0] = H[-1]
    newPos = 0
    #TO BE CONTINUED
    return alpha

def main():
    return

if __name__ == '__main__':
    main()
