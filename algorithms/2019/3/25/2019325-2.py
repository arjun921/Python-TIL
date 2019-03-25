# https://www.hackerrank.com/challenges/capitalize/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    temp = s[0].capitalize()
    print(s[1:])
    s = s[1:]
    for i,c in enumerate(s):
        if str(s[i-1]) == ' ':
            temp += c.capitalize()
        else:
            temp += c
    return temp

if __name__ == '__main__':
    

    s = input()

    result = solve(s)
    print(result)
    

    
