#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-11-24
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from tree_func import TreeNode, generate_tree

# 由于后序遍历的顺序是左右中，我们把它反过来，则遍历顺序变成中右左，
# 是不是跟前序遍历只有左右结点的差异了呢？然而左右的差异仅仅就是.left和.right的差异，在代码上只有机械的差别
def postorderTraversal(root: TreeNode) -> list([int]):
    ans = []
    stack = []

    while stack or root:
        if root:
            ans.append(root.val)
            stack.append(root.left)
            root = root.right
        else:
            root = stack.pop()

    return ans[::-1]

if __name__ == '__main__':
    tree = generate_tree([1,None,2,3])
    print(tree.val)
    print(postorderTraversal(tree))
    print(tree.val)