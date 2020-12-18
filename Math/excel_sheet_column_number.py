#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-19
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

def titleToNumber(s: str) -> int:
    i = 0
    result = 0
    for char in s[::-1]:
        r = ord(char) - ord('A') + 1
        result += r * 26**i
        i += 1

    return result


if __name__ == '__main__':
    print(titleToNumber('AA'))
