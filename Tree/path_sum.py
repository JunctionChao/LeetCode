#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-11-25
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from tree_func import TreeNode, generate_tree

def hasPathSum(root: TreeNode, sum: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == sum

    sum -= root.val
    return hasPathSum(root.left, sum) or hasPathSum(root.right, sum)

if __name__ == '__main__':
    tree = generate_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])
    print(hasPathSum(tree, 22))