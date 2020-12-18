#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-14
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# https://leetcode.com/problems/spiral-matrix-ii/
"""
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
# https://leetcode.com/problems/spiral-matrix-ii/discuss/22443/9-lines-python-solution
def generateMatrix(n: int) -> list([list([int])]):
    result = [[0 for i in range(n)] for j in range(n)]
    coord = [[(i,j) for j in range(n)] for i in range(n)]

    count = 1

    while coord:
        for x, y in coord.pop(0):
            result[x][y] = count
            count += 1
        coord = list(zip(*coord))[::-1]

    return result

# Walk the spiral 
def generateMatrix2(n):
    A = [[0] * n for _ in range(n)]
    i, j, di, dj = 0, 0, 0, 1
    for k in range(n*n):
        A[i][j] = k + 1
        if A[(i+di)%n][(j+dj)%n]:
            di, dj = dj, -di
        i += di
        j += dj

    return A


if __name__ == '__main__':
    print(generateMatrix(3))
    print(generateMatrix(5))
    print(generateMatrix2(3))
    print(generateMatrix2(5))