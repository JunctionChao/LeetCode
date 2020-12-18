#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-18
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

def addBinary(a: str, b: str) -> str:
    i, j = len(a)-1, len(b)-1
    sl = list()
    carry = 0
    while i >= 0 or j >= 0:
        s = carry
        if i >= 0:
            s += int(a[i])
            # s += ord(a[i]) - ord('0') # 这个速度更快
            i -= 1
        if j >= 0:
            s += int(b[j])
            # s += ord(b[j]) - ord('0')
            j -= 1
        carry, mod = divmod(s, 2)
        sl.append(mod)
    if carry:
        sl.append(carry)

    return ''.join(map(str,sl[::-1]))


if __name__ == '__main__':
    print(addBinary('11', '1'))
    print(addBinary('1010', '1011'))