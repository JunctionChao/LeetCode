#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-01-29
# @Author  : Yuanbo Zhao (chaojunction@gmail.com)
# Two Sum


def twoSum(nums, target):
    # l = []
    d = {}
    for index,item in enumerate(nums):
        # d[item] = index
        complement = target-item
        if complement in d:
            return [d[complement],index]
        else:
            d[item] = index

    # for num in nums:
    #   print(num)
    #   complement = target-num
    #   if complement in d.keys() and d[num]!=d[complement]:
    #       return [d[num], d[complement]]
            # l.append(d[num])
            # l.append(d[complement])
    
    # return l


l = twoSum([3,3,2,4],6)
print(l)
# if l:
#   print(l)
# else:
#   print('No solution')
    