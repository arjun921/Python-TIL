# https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

#!/bin/python3

import math
import os
import random
import re
import sys

def get_nth(number,n):
    if number-10**n <0:
        return False
    return number // 10**n %10

def sort_array(arr,unit):
    indexes = [x for x in range(len(arr))]
    temp_arr = [get_nth(x,unit) for x in arr]
    for index,item in enumerate(temp_arr):
        

# Radix sort
def radix_sort(arr):
    max_num = 0
    # replacing max(arr)
    for x in arr:
        if max_num<x:
            max_num=x
    k = len(str(max_num))
    # number of passes = number of digits in max
    for unit in range(k):
        # unit, tens, hundreths digit to sort
        sort_array(arr,unit)

        
        

    


# Complete the maximumToys function below.
def maximumToys(prices, k):
    sorted_ = False
    to_sort = len(prices)-1
    while not sorted_:
        sorted_ = True
        for i in range(to_sort):
            if prices[i]>prices[i+1]:
                #swap (bubble up)
                prices[i],prices[i+1] = prices[i+1],prices[i]
                sorted_ = False
        to_sort -=1
    max_value = 0
    i = 0
    while max_value<=k:
        max_value += prices[i]
        i+=1
    print(i-1)


        

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)




