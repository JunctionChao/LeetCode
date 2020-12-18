#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-16
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

import re

def myAtoi(str: str) -> int:
    str = str.strip()
    str = re.findall('(^[\+\-0]*\d+)\D*', str)
    try:
        result = int(''.join(str))
        return max(-2**31, min(result,2**31-1))
    except:
        return 0


if __name__ == '__main__':
    print(myAtoi("  -42"))
    print(myAtoi("4193 with words 45"))
    print(myAtoi("words and 987"))
    print(myAtoi("-91283472332"))
    print(myAtoi("-0045"))