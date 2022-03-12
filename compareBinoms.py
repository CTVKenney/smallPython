#!/usr/bin/env python3

import math
import sys

def main(k = int(sys.argv[1]), l = int(sys.argv[2]), m = int(sys.argv[3]), n = int(sys.argv[4])):
    """
    Input natural numbers k,l,m,n such that 0 <= l <= k <= l+m <= n-k.
    Check whether {n-k-m \choose k} {n \choose k} \geq {n-k \choose k} {n-l-m \choose k}
    """
    upper = math.comb(n-k-m, k) * math.comb(n, k)
    lower = math.comb(n-k, k) * math.comb(n-l-m, k)
    if upper >= lower:
        print(f'{upper} >= {lower}')
        return True
    else:
        print(f'{upper} < {lower}')
        return False

if __name__ == '__main__':
    main()
