#!/bin/python3
# https://www.hackerrank.com/challenges/minimum-swaps-2/submissions/code/102685145?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# Timeout
import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    start = 0
    end = len(arr)-1
    swaps = 0
    print(arr)
    while start<end:
        print(start,end)
        while arr[start] == start+1 and start<end:
            start+=1
        if start<end:
            # PSA: start and end are indexes. not start/end elements
            # store value that should be at 'start'.
            temp = arr[arr[start]-1]
            # swap value of 'start' at index where 'start' element found
            arr[arr[start]-1] = arr[start]
            #stores value at 'start' from temp
            arr[start] = temp
            swaps += 1
            print(arr)
    return swaps

if __name__ == '__main__':
    cases = {
        'case0': [4,[4,3,1,2],3],
        # 'case1': [5,[2,3,4,1,5],3],
        # 'case2': [7,[1,3,5,2,4,6,7],3]
    }
    for x in cases.items():
        print(f'Test case: {x[0]}')
        n = x[1][0]
        arr = x[1][1]
        y = x[1][2]

        # n = int(input())
        # s = input()
        res = minimumSwaps(arr)
        if y == res:
            print('Passed.')
        else:
            print('Test Failed')
            print(f'Expected: {y}, Got: {res}')
        print('-'*10)

