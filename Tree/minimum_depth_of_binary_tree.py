#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-11-25
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from tree_func import TreeNode, generate_tree

def minDepth(root: TreeNode) -> int:
    if not root:
        return 0
    if not root.left or not root.right:
        return max(minDepth(root.left), minDepth(root.right)) + 1
    else:
        return 1 + min(minDepth(root.left), minDepth(root.right))


if __name__ == '__main__':
    tree = generate_tree([1,None,2,3])
    print(minDepth(tree))