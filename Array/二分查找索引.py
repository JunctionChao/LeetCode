#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-09
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Find First and Last Position of Element in Sorted Array

# returns leftmost (or rightmost) index at which `target` should be inserted in sorted
# array `nums` via binary search.
def extreme_insertion_index(nums: list([int]), target: int, left: bool) -> int:
    lo = 0
    hi = len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > target or (left and target == nums[mid]):
            hi = mid
        else:
            lo = mid + 1

    return lo


def searchRange(nums: list([int]), target: int) -> list([int]):
    left_idx = extreme_insertion_index(nums, target, True)

    # assert that `left_idx` is within the array bounds and that `target`
    # is actually in `nums`.
    if left_idx == len(nums) or nums[left_idx] != target:
        return [-1, -1]

    return [left_idx, extreme_insertion_index(nums, target, False) - 1]


if __name__ == '__main__':
    nums = [5,5,5,5,5,5]
    print(searchRange(nums, 5))

    nums = [5,7,7,8,8,10]
    print(searchRange(nums, 8))
    print(searchRange(nums, 6))
