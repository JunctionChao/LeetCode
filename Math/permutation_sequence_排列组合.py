#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-17
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# https://leetcode.com/problems/permutation-sequence/

import math

def getPermutation(n: int, k: int) -> str:
    numbers = list(range(1, n+1)) # group
    permutation = ''
    k -= 1
    while n > 0:
        n -= 1
        index, k = divmod(k, math.factorial(n))
        permutation += str(numbers[index])

        numbers.remove(numbers[index])

    return permutation


if __name__ == '__main__':
    print(getPermutation(3, 3))
    print(getPermutation(4, 9))