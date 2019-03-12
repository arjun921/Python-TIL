# https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

#!/bin/python3

import math
import os
import random
import re
import sys

"""
Algorithm

sample input:
8
UDDDUDUU

valleys = 0
for step in path
    if step.index < len path
        if step is down and next step is up
            valleys += 1
"""

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys = 0
    altitude = 0
    state = []
    for i in range(n):
        current_step = s[i]
        if current_step == 'U':
            altitude += 1
        if current_step == 'D':
            altitude -= 1
        state.append(altitude)
        if altitude == 0 and current_step == 'U':
            valleys += 1

    # print(state)
    # print(valleys)

    return valleys

if __name__ == '__main__':

    n = int(input())

    s = input()

    result = countingValleys(n, s)
    print(result)
