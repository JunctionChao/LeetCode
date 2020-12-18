#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-20
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

def countPrimes(n: int) -> int:
    if n <= 1:
        return 0
    not_prime = [False] * n
    count = 0
    for i in range(2, n):
        if not not_prime[i]:
            count += 1
            j = 2
            while i*j < n:
                not_prime[i*j] = True
                j += 1

    return count

def countPrimes2(n: int) -> int:
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n, i):
                primes[j] = False

    return sum(primes)

if __name__ == '__main__':
    print(countPrimes(10))
    print(countPrimes2(3))