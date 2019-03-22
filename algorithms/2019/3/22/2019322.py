# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrayss
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    actual = [x+1 for x in range(len(q))]
    index_diff = []
    too_chaotic = False
    for x in actual:
        actual_index = actual.index(x)
        q_index = q.index(x)
        diff = actual_index-q_index
        if diff>2:
            too_chaotic = True
        elif diff>0 and diff <=2:
            index_diff.append(diff)
    if too_chaotic:
        print('Too chaotic')
    else:
        print(index_diff)
        print(sum(index_diff))

if __name__ == '__main__':
    # t = 1

    # for t_itr in range(t):
    #     # n = int(input())

    #     # q = list(map(int, input().rstrip().split()))
    #     n = 5
    #     q = [2,1,5,3,4]

    #     minimumBribes(q)
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
