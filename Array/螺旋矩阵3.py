#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-14
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# https://leetcode.com/problems/spiral-matrix-iii/
def spiralMatrixIII(R: int, C: int, r0: int, c0: int) -> list([list([int])]):
    i, j = r0, c0
    coordinates = [[r0, c0]]
    step_size = 1
    sign = 1
    while len(coordinates) < R*C:
        for _ in range(step_size):
            j += sign
            if i < R and j < C and i >= 0 and j >= 0:
                coordinates.append([i, j])

        for _ in range(step_size):
            i += sign
            if i < R and j < C and i >= 0 and j >= 0:
                coordinates.append([i, j])

        step_size += 1
        sign *= -1

    return coordinates


if __name__ == '__main__':
    print(spiralMatrixIII(R=1, C=4, r0=0, c0=0))
    print(spiralMatrixIII(R=5, C=6, r0=1, c0=4))