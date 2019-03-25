# https://www.hackerrank.com/challenges/dynamic-array/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dynamicArray function below.
def dynamicArray(n, queries):
    seqList =  [[x for x in range(n)] for i in range(n)]
    lastAnswer = 0
    for query in queries:
        print(query)
        query_type = query[0]
        x = query[1]
        y = query[2]
        if query_type == 1:
            ind = ((bool(x) ^ bool(lastAnswer))%n)
            seq = seqList[ind]
            seq.append(y)
        elif query_type == 2:
            ind = ((bool(x) ^ bool(lastAnswer))%n)
            seq = seqList[ind]x
            lastAnswer = seq[int(y%len(seq))]
            print(lastAnswer)
    return lastAnswer

if __name__ == '__main__':

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)



