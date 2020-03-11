#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    
    n = int(input().strip())
    s = input().strip()

    sealevel = 0
    valleycount = 0

    for i in s:
        if i == 'U':
            sealevel += 1
        elif i == 'D':
            sealevel -= 1
        if sealevel == 0:
            if prev < sealevel:
                valleycount += 1
        prev = sealevel

    return valleycount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

