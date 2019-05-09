# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    words_dict = {}
    for word in magazine:
        if word in words_dict:
            words_dict[word] = words_dict[word]+1
        else:
            words_dict[word] = 1
    untraceable = False
    note_count = 0
    for word in note:
        if word in words_dict and words_dict[word]!=0:
            note_count += 1
            words_dict[word] = words_dict[word]-1
    if note_count==len(note):
        untraceable = True

    if untraceable:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
