#!/usr/bin/env python3

import math
import random

"""
Let G = (V,E) be a D-regular graph on 2D vertices. We will take V = {0,1,...,2D-1}.
We can imagine placing these vertices around a circle, and making an edge from each vertex
to the D others nearest to it (so we need D even). We should be able to implement this by connecting
each i \in V to i+k for k=1,2,...D, with i+k computed mod 2D.

Then each neighborhood is different. We now color the vertices of V with colors from Gamma = {0,1,...,D},
independently and uniformly at random. v \in T if \forall w ~ v, color(w) \neq color(v).

The expected size of N_v \intersect T, for any vertex v, is approximately D/e. The program
should return and/or print [#(N_v \intersect T) - D/e]/D, for whichever v maximizes this quantity.
This ratio needs to go to 0 for our approach to be good.
"""

#wellColor inputs a list of colors, one at each vertex,
#and outputs a list of 1s and 0s (1 means well-colored, 0 means ill-colored)
def wellColor(colors):
	D = len(colors)/2 #D should be even
	goods = [1 for i in range(2D)] #each vertex is innocent until proven guilty
	for i in range(2*D):
		for k in range(D/2): #since we want to use 1,2,...,D/2, we'll need to add 1.
			if colors(i) == colors(i+k+1 % 2*D):
				goods(i) = 0
				goods(i+k+1 % 2*D) = 0 #is this the syntax for altering a list?
	return goods

#neighGoods inputs a list of good (1) and bad (0) vertices, as well
#as the index of a particular vertex, and returns the number
#of good vertices in the neighborhood of the given vertex. 
def neighGoods(goods, vertex):
	D = len(goods)/2
	if vertex < D/2:
		needEnd = 2*D + vertex - D/2
		gBefore = sum(goods[:vertex]) + sum(goods[needEnd:])
	else:
		gBefore = sum(goods[:vertex])
	#To be continued!
		

def main(D):
	colors = [random.randrange(D+1) for i in range(2*D)]
	worstVx = 0
	for i in range(2*D):
		

if __name__ == '__main__':
	main()