#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-10-08
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from tree_func import generate_tree, TreeNode

def levelOrder(root: TreeNode) -> list([list([int])]):
    if not root:
        return []
    ans, level = [], [root]
    while level:
        ans.append([node.val for node in level])
        temp = []
        for node in level:
            temp.extend([node.left, node.right])
        level = [leaf for leaf in temp if leaf]

    return ans


def levelOrder1(root: TreeNode) -> list([list([int])]):
    ans, level = [], [root]
    while root and level:
        ans.append([node.val for node in level])
        lr_pair = [(node.left, node.right) for node in level]
        level = [leaf for lr in lr_pair for leaf in lr if leaf]

    return ans 


if __name__ == '__main__':
    tree = generate_tree([3,9,20,None,None,15,7])
    print(levelOrder(tree))