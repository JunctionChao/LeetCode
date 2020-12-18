#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-16
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# https://leetcode.com/problems/reverse-integer/

def reverse(x: int) -> int:
    sign = (x > 0) - (x < 0)
    # sign = [1, -1][x < 0]
    r = int(str(x*sign)[::-1])
    return sign*r * (r < 2**31)

def reverse2(x: int) -> int:
    sign = [1, -1][x < 0]
    rst = sign * int(str(abs(x))[::-1])
    return rst if -(2**31)-1 < rst < 2**31 else 0

def reverse3(x: int) -> int:
    sign = [1, -1][x < 0]
    rev, x = 0, abs(x)
    while x:
        x, mod = divmod(x, 10)
        rev = rev * 10 + mod
    return sign*rev if -pow(2, 31) <= sign*rev <=pow(2, 31)-1 else 0


if __name__ == '__main__':
    print(reverse(83648))
    print(reverse(-143434))
    print(reverse(8463847412))
    print(reverse(7463847412))
    print(reverse(-8463847412))
    print(reverse2(-8463847412))
    print(reverse3(-8463847412))