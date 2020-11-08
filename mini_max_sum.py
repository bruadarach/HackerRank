#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.


def miniMaxSum(arr):
    arr.sort()

    if len(arr) == 5:

        for i in arr:
            if 1 <= i <= 10**9:
                continue
            else:
                break

    print(sum(arr[:4]), sum(arr[-4:]))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
