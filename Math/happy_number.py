#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-20
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

def isHappy(n: int) -> bool:
    seen = set()
    while n not in seen:
        seen.add(n)
        n = sum([int(x) ** 2 for x in str(n)])
    return n == 1


if __name__ == '__main__':
    print(isHappy(19))