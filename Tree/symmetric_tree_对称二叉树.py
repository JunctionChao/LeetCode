#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-10-08
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from tree_func import generate_tree, TreeNode

# recursive
def isSymmetric(root: TreeNode) -> bool:

    def isSymmetric_help(left, right):
        if left is None or right is None:
            return left==right
        if left.val != right.val:
            return False
        return isSymmetric_help(left.left, right.right) and isSymmetric_help(left.right, right.left)

    return root is None or isSymmetric_help(root.left, root.right)


# stack
def isSymmetric1(root: TreeNode) -> bool:
    if root is None:
        return True
    stack = [(root.left, root.right)]

    while stack:
        left, right = stack.pop()
        if left is None and right is None:
            continue
        if left is None or right is None:
            return False
        if left.val == right.val:
            stack.append((left.left, right.right))
            stack.append((left.right, right.left))
        else:
            return False
    return True


if __name__ == '__main__':
    tree = generate_tree([1, 2, 2, 3, 4, 4, 3])
    print(isSymmetric(tree))
    print(isSymmetric1(tree))