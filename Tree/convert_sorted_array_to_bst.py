#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-11-25
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from tree_func import TreeNode, generate_tree

def sortedArrayToBST(nums: list([int])) -> TreeNode:
    if not nums:
        return None

    mid = len(nums) // 2

    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])

    return root

if __name__ == '__main__':
    sorted_array = [-10,-3,0,5,9]
    tree = sortedArrayToBST(sorted_array)