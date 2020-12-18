#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-16
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

def isPalindrome(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x!= 0):
        return False

    revertedNumber = 0
    while x > revertedNumber:
        revertedNumber = revertedNumber * 10 + x % 10
        x //= 10

    return x == revertedNumber or x == revertedNumber // 10

def isPalindromePythonic(x: int) -> bool:
    return str(x) == str(x)[::-1]


if __name__ == '__main__':
    print(isPalindrome(121))
    print(isPalindrome(-121))
    print(isPalindrome(10))

    print(isPalindromePythonic(121))
    print(isPalindromePythonic(-121))
    print(isPalindromePythonic(10))