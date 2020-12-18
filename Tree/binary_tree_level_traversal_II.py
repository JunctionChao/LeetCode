#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-10-08
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from tree_func import generate_tree, TreeNode

def levelOrderBottom(root: TreeNode) -> list([list([int])]):
    if not root:
        return []
    ans, level = [], [root]
    while level:
        ans.append([node.val for node in level])
        temp = []
        for node in level:
            temp.extend([node.left, node.right])
        level = [leaf for leaf in temp if leaf]

    return ans[::-1]

# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/discuss/34978/Python-solutions-(dfs-recursively-dfs%2Bstack-bfs%2Bqueue).

# dfs recurisvelly
def levelOrderBottom1(root: TreeNode) -> list([list([int])]):

    def dfs(root, level, res):
        if root:
            if len(res) < level + 1:
                res.insert(0, [])
            res[-(level+1)].append(root.val)
            dfs(root.left, level+1, res)
            dfs(root.right, level+1, res)

    res = []
    dfs(root, 0, res)
    return res

# dfs + stack
def levelOrderBottom2(root: TreeNode) -> list([list([int])]):
    stack = [(root, 0)]
    res = []
    while stack:
        node, level = stack.pop()
        if node:
            if len(res) < level+1:
                res.insert(0, [])
            res[-(level+1)].append(node.val)
            stack.append((node.right, level+1))
            stack.append((node.left, level+1))
    return res

if __name__ == '__main__':
    tree = generate_tree([3,9,20,None,None,15,7])
    print(levelOrderBottom(tree))