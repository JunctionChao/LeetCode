#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-18
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# 最大公约数GCD 最小公倍数LCM
# LCM(A,B)×GCD(A,B)=A×B
"""性质

如果b是A和B的公约数，那么：

b也是A+B的约数，即b是A,B,A+B的公约数
b也是A-B的约数，即b是A,B,A-B的公约数
更一般地，对于任意整数x、y，b也是Ax+By的约数，即b是A,B,Ax+By的公约数
根据上一条性质，r = A - kB = A mod B，所以A mod B也是A+B的约数，mod是求余运算，即b是A,B,A mod B的公约数

gcd(A, B) = gcd(B, A mod B)   其中:A > B
"""
# 辗转相除法
def gcd_1(a, b):

    while b > 0:
        r = a % b
        a = b
        b = r

    return a

# 递归
def gcd_2(a, b):
    if b == 0:
        return a
    return gcd_2(b, a%b)


if __name__ == '__main__':
    print(gcd_1(27, 18))
    print(gcd_2(27, 18))
    print(gcd_2(18, 27))