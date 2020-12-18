#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-08-17
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# 方案1
def removeDuplicates(nums: list()) -> (int, list()):
    length = len(nums)

    current = 0
    next_ = 1

    while next_ < length:
        currNum = nums[current]
        nextNum = nums[next_]
        if currNum != nextNum:
            current += 1
            nums[current] = nums[next_]
        next_ += 1

    return current + 1, nums


from collections import OrderedDict
def removeDuplicates2(nums):
    nums[:] = OrderedDict.fromkeys(nums)
    return len(nums), nums


def removeDuplicates3(nums):
    if len(nums) < 2:
        return len(nums)
    
    j = 0
    
    for num in nums[1:]:
        if num != nums[j]:
            j += 1
            nums[j] = num
    return j+1


if __name__ == '__main__':

    nums = [0,0,1,1,1,2,2,3,3,4]
    # length, nums = removeDuplicates(nums)
    print(removeDuplicates(nums))

    print(removeDuplicates2(nums))
