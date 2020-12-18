#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-01
# @Author  : Yuanbo Zhao (chaojunction@gmail.com)
# Three Sum
'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.
'''

def threeSum(nums):
    result = []
    nums.sort()
    for i in range(len(nums)-2):
        #若出现相邻相同的数，则以前者为基础的后续搜索循环内包含了以后者为基础的搜索循环
        #所以直接跳过
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1, len(nums)-1
        while left < right:
            sum = nums[i]+nums[left]+nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                result.append([nums[i],nums[left],nums[right]])
                while left < right and nums[left] == nums[left+1]:#相邻相同重复
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1; right -= 1
    return result

if __name__ == '__main__':
    nums = [2,4,-3,7,-1,3,5,0,6,-4]
    print(threeSum(nums))