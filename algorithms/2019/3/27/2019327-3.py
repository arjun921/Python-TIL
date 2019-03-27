# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter
from itertools import combinations

# def get_anagrams(s):
    

#     return anagrams_list

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    leng = len(s)-1
    pieces = set()
    for i in range(leng):
        for j in range(leng+1):
            print(s[i:j])
            # if len(combination)>=1:
            #     pieces.add(combination)
            #     print(combination)
    # for i in pieces:
    count = 0
    """
    for all pieces whose length is same, check if each is anagram.
    # """

    # pieces = list(pieces)
    # leng = len(pieces)-1
    # for i in range(0,leng,1):
    #     for j in range(leng,0,-1):
    #         f_item = pieces[i]
    #         b_item = pieces[j]
    #         # if len(f_item)==len(b_item):
    #         if Counter(f_item)==Counter(b_item):

    #             print(f_item,b_item)
        

    # for i,item in enumerate():
    #     if len(item)==
    #     # if item[1]==1:
    #     #     count += 1
    #     #     print(item)
    # print(count)



if __name__ == '__main__':

    # q = int(input())

    # for q_itr in range(q):
    #     s = input()

    result = sherlockAndAnagrams('abba')
    # result = sherlockAndAnagrams('ifailuhkqq')

    #     print(str(result))

