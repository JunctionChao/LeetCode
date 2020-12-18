#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-10-01
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

def uniquePaths(m: int, n: int) -> int:
    path = [[1] * n for i in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            path[i][j] = path[i-1][j] + path[i][j-1]

    return path[-1][-1]


if __name__ == '__main__':
    print(uniquePaths(3, 2))
    print(uniquePaths(7, 3))