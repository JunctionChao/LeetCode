#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-16
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

def divide(dividend: int, divisor: int) -> int:
    sign = (dividend < 0) == (divisor < 0)
    dividend, divisor, res = abs(dividend), abs(divisor), 0
    while dividend >= divisor:
        temp, i = divisor, 1
        while dividend >= temp:
            dividend -= temp
            res += i
            i <<= 1
            temp <<= 1

    if not sign:
        res = -res

    return min(max(-2**31, res), 2**31-1)


if __name__ == '__main__':
    print(divide(10, 3))
    print(divide(7, -3))