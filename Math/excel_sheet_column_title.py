#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-19
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

def convertToTitle(n: int) -> str:
    capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
    result = []
    while n > 0:
        result.append(capitals[(n-1)%26])
        n = (n-1) // 26
    result.reverse()
    return ''.join(result)


def convertToTitleOneLine(n: int) -> str:
    return "" if n == 0 else convertToTitleOneLine((n - 1)//26) + chr((n -1)%26 + ord('A'))


if __name__ == '__main__':
    print(convertToTitle(701))
    print(convertToTitleOneLine((701)))