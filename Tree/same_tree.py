#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-10-08
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from tree_func import TreeNode, generate_tree

def isSameTree(p: TreeNode, q: TreeNode) -> bool:
    if not p and not q:
        return True
    if p is None or q is None:
        return False
    if p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    return False

def isSameTree1(p: TreeNode, q: TreeNode) -> bool:
    if p and q:
        return p.val == q.val and isSameTree1(p.left, q.left) and isSameTree1(p.right, q.right)

    return p is q # It is just to return True if p==None and q==None else False.


if __name__ == '__main__':
    p = generate_tree([1,2,3])
    q = generate_tree([1,2,3])
    print(isSameTree(p, q))