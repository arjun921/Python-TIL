#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.

def formingMagicSquare(s):
    cost = 0
    magic_square = [[8,3,4],[1,5,9],[6,7,2]]
    return cost


if __name__ == '__main__':

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    print(result)
