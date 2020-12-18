#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-18
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# 牛顿迭代法 http://www.matrix67.com/blog/archives/361
def mySqrt(x: int) -> int:
    r = x
    while r*r > x:
        r = (r + x//r) //2
    return r


if __name__ == '__main__':
    print(mySqrt(17))
