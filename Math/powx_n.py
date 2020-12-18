#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-16
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# Iterative
def myPow1(x: float, n: int) -> float:
    if n < 0:
        x = 1 / x
        n = -n
    _pow = 1
    while n:
        if n & 1: # 奇数
            _pow *= x
        x *= x
        n >>= 1
    return _pow

# Recursive
def myPow2(x: float, n: int) -> float:
    if not n:
        return 1
    if n < 0:
        return 1 / myPow2(x, -n)
    if n % 2:
        return x * myPow2(x, n-1)

    return myPow2(x*x, n/2)


if __name__ == '__main__':
    print(myPow1(4.3, 2))