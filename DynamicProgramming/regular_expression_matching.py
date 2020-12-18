#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-21
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# https://leetcode.com/problems/regular-expression-matching/discuss/5651/Easy-DP-Java-Solution-with-detailed-Explanation

def isMatch(self, s: str, p: str) -> bool:
    m, n = len(s), len(p)
    f = [[False] * (n+1) for _ in range(m+1)]
    f[0][0] = True
    # p[0.., j - 3, j - 2, j - 1] matches empty iff p[j - 1] is '*' and p[0..j - 3] matches empty
    for j in range(2, n+1):
        f[0][j] = p[j-1] == '*' and f[0][j-2];

    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] != '*':
                f[i][j] = f[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == '.')
            else:
                f[i][j] = f[i][j-2] or ((s[i-1] == p[j-2] or p[j-2] == '.') and f[i-1][j])
                
    return f[m][n]


if __name__ == '__main__':
    print(isMatch())