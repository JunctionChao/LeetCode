#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-08-17
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# https://leetcode.com/problems/container-with-most-water/

def maxArea(height: list()) -> int:
    maxarea = 0
    l = 0
    r = len(height) - 1
    while l < r:
        maxarea = max(maxarea, min(height[l], height[r]) * (r-l))
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return maxarea

if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))
