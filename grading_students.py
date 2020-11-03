#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):

    final = []

    for grade in grades:

        if 0 <= grade <= 100:

            next_multiple = ((grade // 5) + 1) * 5
            difference = next_multiple - grade

            if grade < 38:
                final.append(grade)

            elif difference < 3:
                final.append(next_multiple)

            else:
                final.append(grade)

    return final


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
