#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-10-08
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from tree_func import TreeNode, generate_tree

def sumOfLeftLeaves(root: TreeNode) -> int:
    if not root:
        return 0
    if root.left and not root.left.left and not root.left.right:
        return root.left.val + sumOfLeftLeaves(root.right)
    return sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right)


if __name__ == '__main__':
    tree = generate_tree([3,9,20,None,None,15,7])
    print(sumOfLeftLeaves(tree))