#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    a = 0
    i = 0
    j = 0
    while i < len(arr):
        while j < len(arr):
            a += arr[i][j]
            j += 1
            i += 1
            
    b = 0
    i = 0
    k = len(arr)-1
    while i < len(arr): 
        while k >= 0:
            b += arr[i][k]
            k -= 1
            i += 1
          
    return abs(a-b)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()


"""
my_sum1 = 0
    my_sum2 = 0
    for i in range(len(arr)):
        my_sum1 += arr[i][i]
        my_sum2 += arr[i][len(arr)-i-1]
    ans = my_sum1-my_sum2
    return abs(ans)
"""


"""
d1 = sum([a[x][x] for x in range(n)]) 
d2 = sum([a[x][n-1-x] for x in range (n)])
print(abs(d1-d2))
"""


"""
import math
n = int(input())
square = []
difference = 0
leftdi = 0
rightdi = 0
for i in range(n):
    square.append(input().split())
    leftdi += int(square[i][i])
    rightdi += int(square[i][-i-1])
print(abs(leftdi-rightdi))
"""