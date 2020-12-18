#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-19
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# https://leetcode.com/problems/factorial-trailing-zeroes/discuss/196311/topic
# 给定整数n，返回n!中尾随零的数目

# 递归
def trailingZeroes(n: int) -> int:
    if n == 0:
        return 0
    else:
        return n // 5 + trailingZeroes(n//5)

# 非递归
def trailingZeroes2(n: int) -> int:
    result = 0
    while n > 0:
        result += n//5
        n //= 5
    return result


if __name__ == '__main__':
    print(trailingZeroes(5))
    print(trailingZeroes2(25))