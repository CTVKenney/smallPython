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
#integer is an integer we want to add as a new element
def hInsert(integer, H):
    newList = H + [integer]
    #TO BE CONTINUED

def main():
    return

if __name__ == '__main__':
    main()
