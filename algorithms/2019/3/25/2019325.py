# https://www.hackerrank.com/challenges/dynamic-array/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dynamicArray function below.
def dynamicArray(n, queries):
    seqList =  [[] for i in range(n)]
    lastAnswer = 0
    lastAnswers = []
    for query_type,x,y in queries:
        ind = (x ^ lastAnswer)%n
        seq = seqList[ind]
        if query_type == 1:
            seq.append(y)
        elif query_type == 2:
            number = y%len(seq)
            lastAnswer = seq[number]
            lastAnswers.append(lastAnswer)
    return lastAnswers

if __name__ == '__main__':

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)
    print('\n'.join(map(str,result)))


