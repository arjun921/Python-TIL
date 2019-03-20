# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    l = len(s)
    c = s.count('a')
    if c>1:
        count = round((c*n)/l)
    else:
        count = int((c*n)/l)
    print((c*n)/l)
    print(s[:n % len(s)].count("a"))
    return count

if __name__ == '__main__':

    s = input()

    n = int(input())

    result = repeatedString(s, n)
    print(result)

