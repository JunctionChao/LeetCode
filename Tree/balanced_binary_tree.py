#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-11-25
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from tree_func import TreeNode, generate_tree


def isBalanced(root: TreeNode) -> bool:

    def check(root: TreeNode) -> int:
        if not root:
            return 0
        hl = check(root.left) + 1
        hr = check(root.right) + 1
        if abs(hl - hr) > 1 or hl == 0 or hr == 0:
            return -1
        return max(hl, hr)

    return check(root) != -1


def isBalanced_readable(root: TreeNode) -> bool:

    def check(root: TreeNode) -> (int, bool):
        if not root:
            return 0, True
        l_depth, l_balanced = check(root.left)
        r_depth, r_balanced = check(root.right)
        return max(l_depth, r_depth) + 1, l_balanced and r_balanced and abs(l_depth - r_depth) <= 1

    return check(root)[1]

if __name__ == '__main__':
    tree = generate_tree([3,9,20,None,None,15,7])
    print(isBalanced(tree))