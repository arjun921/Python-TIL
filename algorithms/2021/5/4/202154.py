#!/bin/python3

# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def get_char_count(s):
    chars_count = {}
    for x in s:
        if x in chars_count:
            chars_count[x] += 1
        else:
            chars_count[x] = 1
    return chars_count
        

def isValid(s):
    # Write your code here
    if len(s)==1:
        return 'YES'
    
    chars_count = get_char_count(s)
    counts = [str(x) for x in chars_count.values()]
    counts_count = get_char_count(''.join(counts))
    print(chars_count)
    print(counts_count)
    if len(counts_count)>2:
        return 'NO'
    if '1' in counts_count:
        if counts_count['1']==1:
            return 'YES'
    if '3' in counts_count:
        if counts_count['3']==1:
            return 'YES'
    inverted_chars = {}
    for key,val in chars_count.items():
        if val not in inverted_chars:
            inverted_chars[val] = key
        else:
            old = inverted_chars[val]
            if type(old) is not list:
                old = [old]
            inverted_chars[val] = old + [key]
    
    try:
        if len(inverted_chars[1])==1:
            return 'YES'
    except Exception as e:
        pass
    print(inverted_chars)
    if len(inverted_chars)==1:
        return 'YES'
    return 'NO'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
