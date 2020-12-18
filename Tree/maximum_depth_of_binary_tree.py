#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-11-24
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from tree_func import TreeNode, generate_tree

def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    else:
        return 1 + max(maxDepth(root.left), maxDepth(root.right))


if __name__ == '__main__':
    tree = generate_tree([1,None,2,3])
    print(maxDepth(tree))