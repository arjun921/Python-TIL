#!/bin/python3
# https://www.hackerrank.com/challenges/compare-the-triplets/problem
# Two Tries
import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    score_a = 0
    score_b = 0
    for x in zip(a,b):
        if x[0]>x[1]:
            score_a += 1
        elif x[0]<x[1]:
            score_b += 1
    return [score_a,score_b]

if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(result)