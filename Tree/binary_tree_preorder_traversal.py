#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-11-24
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from tree_func import TreeNode, generate_tree

def preorderTraversal(root: TreeNode) -> list([int]):
    ans = []
    stack = []

    while stack or root:
        if root:
            ans.append(root.val)
            stack.append(root.right)
            root = root.left
        else:
            root = stack.pop()

    return ans

if __name__ == '__main__':
    tree = generate_tree([1,None,2,3])
    print(tree, tree.right)
    print(tree)
    print(preorderTraversal(tree))
    print(tree)