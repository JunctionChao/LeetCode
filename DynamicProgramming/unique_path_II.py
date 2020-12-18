#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-10-01
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

def uniquePathsWithObstacles(obstacleGrid: list([list([int])])) -> int:
    if obstacleGrid[0][0] == 1:
        return 0
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    label_i = label_j = 1
    for i in range(m):
        if obstacleGrid[i][0] == 1:
            label_i = 0
        obstacleGrid[i][0] = label_i

    for j in range(1, n):
        if obstacleGrid[0][j] == 1:
            label_j = 0
        obstacleGrid[0][j] = label_j

    for i in range(1, m):
        for j in range(1, n):
            if obstacleGrid[i][j] == 1:
                obstacleGrid[i][j] = 0
            else:
                obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]

    return obstacleGrid[-1][-1]


if __name__ == '__main__':
    obstacleGrid = [
                    [0,0,0],
                    [0,1,0],
                    [0,0,0]
                   ]
    print(uniquePathsWithObstacles(obstacleGrid))