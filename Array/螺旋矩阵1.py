#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-13
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# https://leetcode.com/problems/spiral-matrix/

"""
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
"""

def spiralOrder(matrix: list([list([int])])) -> list([int]):
    if not matrix:
        return []
    R, C = len(matrix), len(matrix[0])
    seen = [[False] * C for _ in matrix]
    ans = []
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r = c = di = 0
    for _ in range(R * C):
        ans.append(matrix[r][c])
        seen[r][c] = True
        cr, cc = r + dr[di], c + dc[di]
        if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
            r, c = cr, cc
        else:
            di = (di + 1) % 4
            r, c = r + dr[di], c + dc[di]
    return ans

# https://leetcode.com/problems/spiral-matrix/discuss/20571/1-liner-in-Python-%2B-Ruby
def spiralOrderOneLine(matrix):
    return matrix and [*matrix.pop(0)] + spiralOrderOneLine([*zip(*matrix)][::-1])

if __name__ == '__main__':
    matrix1 = [[ 1, 2, 3 ],
               [ 4, 5, 6 ],
               [ 7, 8, 9 ]]
    matrix2 = [[ 1, 2, 3 ]]
    print(spiralOrder(matrix1))
    print(spiralOrder(matrix2))

    print(spiralOrderOneLine(matrix1))
    print(spiralOrderOneLine(matrix2))