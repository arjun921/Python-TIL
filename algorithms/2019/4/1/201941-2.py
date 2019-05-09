# https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen
#!/bin/python3
# copied from discussions. couldn't come up with solution that didn't timeout.

import math
import os
import random
import re
import sys

from collections import defaultdict
# Complete the freqQuery function below.
def freqQuery(queries):
    ds = {}
    print_list = []
    freqs = defaultdict(set)
    for query in (queries):
        qtype,val = query[0],query[1]
        freq = ds.get(val, 0)
        if qtype == 1:
            ds[val] = freq + 1
            freqs[freq].discard(val)
            freqs[freq+1].add(val)
        elif qtype == 2:
            ds[val] = max(0,freq - 1)
            freqs[freq].discard(val)
            freqs[freq-1].add(val)
        else:    
            print_list.append(1 if freqs[val] else 0)
    return print_list


if __name__ == '__main__':

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    print('\n'.join(map(str, ans)))

