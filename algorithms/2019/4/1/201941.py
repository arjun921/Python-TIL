# https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
#!/bin/python3

import math
import os
import random
import re
import sys
# failed to solve myself.

# Complete the countTriplets function below.
def countTriplets(arr, r):
    # initialize the dictionaries
    r2 = {}
    r3 = {}
    count = 0

    # loop throgh the arr itens
    for k in arr:
        # if k in r3 indicates the triplet already completed,
        # the count need be incremented
        next_elem = k*r
        if k in r3:
            count += r3[k]

        # if k in r2, it is the secound number of the triplet,
        # your successor (third element k*r) need be added or incremented in the r3 dict
        # because is a potencial triplet 
        if k in r2:
            r3[next_elem] = r3.get(next_elem, 0) + r2[k]

        # else, k is the first element of the triplet, so,
        # your seccessor (secound element next_elem) need be added or incremented in the r2 dict
        # because is a potencial triplet
        r2[next_elem] = r2.get(next_elem, 0) + 1

    return count

if __name__ == '__main__':

    nr = input().rstrip().split()
    n = int(nr[0])
    r = int(nr[1])
    arr = list(map(int, input().rstrip().split()))
    ans = countTriplets(arr, r)
    print(ans)

