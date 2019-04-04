# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    sorted_ = False
    unsorted_length = len(a)-1
    swaps = 0
    while not sorted_:
        sorted_ = True
        for i in range(unsorted_length):
            if a[i]>a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
                sorted_ = False
                swaps +=1 
        unsorted_length -=1
    print(f'Array is sorted in {swaps} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[-1]}')




if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
