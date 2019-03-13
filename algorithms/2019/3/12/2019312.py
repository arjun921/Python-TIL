#!/bin/python3

# https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sock_count = 0
    ar.sort()
    while len(ar)>0:
        if ar[0] in ar[1:]:
            if ar[0] == ar[1]:
                sock_count += 1
                del ar[0:2]
        else:
            del ar[0]
    return sock_count

if __name__ == '__main__':

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)


