#!/usr/bin/env python3

import sys

def main():
    k = int(sys.argv[1]) #How high up we'll be summing
    prods = []
    for i in range(k):
        for j in range(i+1,k):
            for l in range(j+1,k):
                prods.append(i*j*l)
    sol = sum(prods)
    print(sol)
    return sol

if __name__ == '__main__':
    main()
