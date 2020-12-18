#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-08-17
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6
"""

import pysnooper

def maxsum(nums):
    max_pre = -float('inf')
    max_cur = -float('inf')
    for num in nums:
        max_cur = max(max_cur + num, num) 
        max_pre = max(max_pre, max_cur)
    return max_pre

# @pysnooper.snoop()
def maxsum_index(nums):
    max_pre = -float('inf')
    max_cur = -float('inf')
    start, end = 0, 0
    flag = False # 表示还是之前max_pre的值最大的标志
    for i, num in enumerate(nums):
        if max_cur + num <= num and not flag:
            start = i
            max_cur = num
        else:
            max_cur = max_cur + num
            
        if max_pre < max_cur:
            end = i
            max_pre = max_cur
            flag = not flag
        
    return [start, end]


if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    # nums = [1, 0, -1, -3, -5]
    print(maxsum(nums))
    print(maxsum_index(nums))