# https://www.hackerrank.com/challenges/python-time-delta/problem
#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

def parser(dt):
    # Sun 10 May 2015 13:54:36 -0700
    dtformat = '%a %d %b %Y %H:%M:%S %z'
    return datetime.strptime(dt,dtformat)
    

# Complete the time_delta function below.
def time_delta(t1, t2):
    t1 = parser(t1)
    t2 = parser(t2)
    diff = t1-t2
    return str(abs(int(diff.total_seconds())))



if __name__ == '__main__':

    t = int(input())
    results = []
    for t_itr in range(t):
        t1 = input()
        t2 = input()

        delta = time_delta(t1, t2)
        results.append(delta)

    for x in results:
        print(x)

