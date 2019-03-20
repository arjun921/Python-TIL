# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

#!/bin/python3
# FAIL

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count_in_single = s.count('a')
    len_single= len(s)
    if count_in_single == len(s):
        return n
    else:
        count = count_in_single * (n // len_single) + s[:n % len_single].count("a")
    return int(count)

if __name__ == '__main__':

    s = input()

    n = int(input())

    result = repeatedString(s, n)
    print(result)

