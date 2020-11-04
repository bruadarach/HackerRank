#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.


def plusMinus(arr):
    #n = len(arr)
    num = {'pos': 0, 'neg': 0, 'zero': 0}

    for i in arr:

        if i > 0:
            num['pos'] += 1

        elif i == 0:
            num['zero'] += 1
            
        else:
            num['neg'] += 1

    for j, count in num.items():
        print(format((count/n), '.6f'))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
