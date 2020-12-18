#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-10-08
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from tree_func import TreeNode, generate_tree

def inorderTraversal(root: TreeNode) -> list([int]):
    ans = []
    stack = []

    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            tmp_node = stack.pop()
            ans.append(tmp_node.val)
            root = tmp_node.right

    return ans

if __name__ == '__main__':
    tree = generate_tree([1,None,2,3])
    print(inorderTraversal(tree))