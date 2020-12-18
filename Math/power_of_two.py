#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-20
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

def isPowerOfTwo(n: int) -> bool:
    while n > 1:
        n /= 2
    if n == 1:
        return True
    else:
        return False

def isPowerOfTwo2(n: int) -> bool:
    return n > 0 and not (n & n-1)


if __name__ == '__main__':
    print(isPowerOfTwo(218))
    print(isPowerOfTwo2(218))