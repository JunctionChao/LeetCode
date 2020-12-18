#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-11-25
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from tree_func import TreeNode, generate_tree

def invertTree(root: TreeNode) -> TreeNode:
    if root:
        root.left, root.right = invertTree(root.right), invertTree(root.left)
        return root


# And an iterative version using stack:
def invertTreeStack(root: TreeNode) -> TreeNode:
    stack = [root]
    while stack:
        node = stack.pop()
        if node:
            node.left, node.right = node.right, node.left
            stack += node.left, node.right
    return root