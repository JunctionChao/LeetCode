#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-04
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# http://bookshadow.com/weblog/2015/08/12/leetcode-zigzag-conversion/
import operator
from functools import reduce

def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    zigzag = [[] for x in range(numRows)]
    row, step = 0, 1
    for c in s:
        zigzag[row] += [c]
        if row == 0:
            step = 1
        elif row == numRows - 1:
            step = -1
        row += step

    return ''.join(reduce(operator.add, zigzag))


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    print(convert(s,3))