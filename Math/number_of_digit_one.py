#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-20
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# https://www.cnblogs.com/grandyang/p/4629032.html

def countDigitOne(n: int) -> int:
    ones, m = 0, 1
    while m <= n:
        ones += (n//m + 8) // 10 * m + (n//m % 10 == 1) * (n%m + 1)
        m *= 10
    return ones

if __name__ == '__main__':
    print(countDigitOne(13))
    print(countDigitOne(124))