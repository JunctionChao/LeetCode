#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-16
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# https://leetcode.com/problems/multiply-strings/
def multiply(num1: str, num2: str) -> str:
    m, n = len(num1), len(num2)
    pos = [0] * (m+n)

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            p1, p2 = i+j, i+j+1
            s = mul + pos[p2]

            pos[p1] += s//10
            pos[p2] = s%10

    index = 0
    while index < len(pos) and pos[index] == 0:
        index += 1

    return '0' if index == len(pos) else ''.join(map(str, pos[index:]))


if __name__ == '__main__':
    print(multiply('4', '26'))
    print(multiply('24', '26'))
    print(multiply('25', '0'))
