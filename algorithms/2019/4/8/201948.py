#!/bin/python3

import math
import os
import random
import re
import sys
# failed to solve
# Complete the makeAnagram function below.

def makeAnagram(a, b):
    count = 0
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabets:
        ia = a.count(letter)
        ib = b.count(letter)
        count += abs(ia - ib)
    return count


if __name__ == '__main__':

    a = 'cde'
    b = 'abc'
    res = makeAnagram(a, b)
    print(res)


