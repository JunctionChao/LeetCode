#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-03
# @Author  : Yuanbo Zhao (chaojunction@gmail.com)
# convert roman num to integer

def romanToInt1(s):
    d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    res = 0
    for i, letter in enumerate(s):
        if (i+1) < len(s):
            if d[s[i]] < d[s[i+1]]:
                res-=d[s[i]]
                # print(res)
            else:
                res+=d[s[i]]
                # print(res)
    return res+d[s[len(s)-1]]
    
def romanToInt2(s):
    d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    res, p = 0, 'I'
    for c in s[::-1]:
        res, p = res - d[c] if d[c] < d[p] else res + d[c], c #替换每次访问多个以下标访问方式的方法
    return res


if __name__ == '__main__':
    print(romanToInt1('VXD'))
    print(romanToInt2('VXD'))