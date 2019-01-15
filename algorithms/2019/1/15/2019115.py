#!/bin/python3
# https://www.hackerrank.com/challenges/simple-array-sum/problem
# Algorithms
import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    a = 0
    for x in ar:
        a+=x
    return a

if __name__ == '__main__':
    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)
    print(result)