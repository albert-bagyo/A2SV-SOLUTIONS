#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    
   
    def swap(i, j):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        
        
    count = 0
    for _ in range(n):
        for i in range(n - 1):
            if a[i] > a[i + 1]:
                swap(i, i + 1)
                count += 1
    
    print(f'Array is sorted in {count} swaps.\nFirst Element: {a[0]}\nLast Element: {a[-1]}')

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
