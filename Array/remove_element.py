#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-05
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# https://leetcode.com/problems/remove-element/

def removeElement(nums: list([int]), val: int) -> int:
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1
    return count

if __name__ == '__main__':
    nums1 = [3,2,2,3]
    nums2 = [0,1,2,2,3,0,4,2]

    print(removeElement(nums1, 3))
    print(removeElement(nums2, 2))