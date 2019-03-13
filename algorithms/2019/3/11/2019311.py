#!/bin/python3
#https://www.hackerrank.com/challenges/a-very-big-sum/problem

import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    return sum(ar)

if __name__ == '__main__':
    
    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)
    print(result)
    