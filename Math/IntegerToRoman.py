#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-16
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

def intToRoman(num: int) -> str:
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    res, i = "", 0
    while num:
        res += (num // values[i]) * numerals[i]
        num %= values[i]
        i += 1

    return res


if __name__ == '__main__':
    print(intToRoman(800))
    print(intToRoman(1994))