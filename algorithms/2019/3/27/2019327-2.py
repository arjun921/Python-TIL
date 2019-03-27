# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
#my solution
def twoStrings(s1, s2):
    subset = False
    for x in s2:
        if x in s1:
            subset = True
            break
    if subset:
        return 'YES'
    else:
        return 'NO'

# Alternate solution
def alternateTwoStrings(s1, s2):
    # create sets of unique characters
    # and test for intersection
    if set(s1)&set(s2):
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s1 = input()
        s2 = input()
        result = twoStrings(s1, s2)
        print(result)