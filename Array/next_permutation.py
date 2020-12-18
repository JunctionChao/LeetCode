#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-07
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# http://bookshadow.com/weblog/2016/09/09/leetcode-next-permutation/

def nextPermutation(nums: list([int])) -> None:
    """
        Do not return anything, modify nums in-place instead.
    """
    size = len(nums)
    for x in range(size-1, -1, -1):
        if nums[x-1] < nums[x]:
            break
    if x > 0:
        for y in range(size-1, -1, -1):
            if nums[y] > nums[x-1]:
                nums[x-1], nums[y] = nums[y], nums[x-1]
                break
    for z in range((size-x)//2):
        nums[x+z], nums[size-z-1] = nums[size-z-1], nums[x+z]


if __name__ == '__main__':
    nums1 = [1,2,3]
    nums2 = [4,3,2,1]
    nums3 = [1,2,5,4,3]
    nextPermutation(nums1)
    nextPermutation(nums2)
    nextPermutation(nums3)
    print(nums1, nums2, nums3, sep='\n')