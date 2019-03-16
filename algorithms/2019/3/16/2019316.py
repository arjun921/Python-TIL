#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

"""
ALgorithm
current_index = 0
while in steps range
    if passed_ind == step_ind:
        break
    if step is end
        exit
    if step is 1 or if step has passed(step index < current index).
        pass
    else
        skip2 = step_i + 2
        skip1 = step_i + 1
        # if iter 0:
        #     passed append step_i
        if skip2 exists and is safe
            current_index = skip2ind
            jump
            pass
        else if skip 1 is safe
            current_index = skip1ind
            jump
            pass
return jump
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    current_index = 0
    step_i = 0
    jump = 0
    while step_i < len(c):
        step = c[step_i]
        if step == 1 or step_i<current_index:
            pass
        else:
            skip2 = step_i+2
            skip1 = step_i+1

            if skip2 < len(c) and c[skip2]!=1:
                current_index = skip2
                jump += 1
            elif skip1< len(c) and c[skip1]!=1:
                current_index = skip1
                jump += 1
        step_i += 1
    return jump


if __name__ == '__main__':

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    print(result)

