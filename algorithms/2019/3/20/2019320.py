# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
#!/bin/python3

import math
import os
import random
import re
import sys


def row_hour_glass(arr,row_index):
    first_line = row_index
    second_line = row_index+1
    third_line = row_index+2
    start = 0
    end = 3
    row = {}
    for _ in range(4):
        mid = end-2
        line_1 = arr[first_line][start:end]
        line_2 = arr[second_line][mid]
        line_3 = arr[third_line][start:end]
        str_hour = ' '.join(map(str,line_1))
        str_hour += f'\n  {line_2}'
        str_hour += '\n'+' '.join(map(str,line_3))
        row[str_hour] = sum(line_1)+line_2+sum(line_3)
        start += 1
        end += 1
    return row


# Complete the hourglassSum function below.
def hourglassSum(arr):
    hour_glasses = {}
    for row_index in range(4):
        row = row_hour_glass(arr,row_index)
        hour_glasses.update(row)
    sorted_hour_glasses = sorted(hour_glasses.items(), key=lambda x:x[1])
    max_val = hour_glasses[sorted_hour_glasses[-1][0]]
    return max_val

if __name__ == '__main__':

    arr = []

    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))
    arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
    result = hourglassSum(arr)
    print(result)


