#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-10-08
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 利用层次遍历原理构建二叉树
def generate_tree(level_traver_list):
    if not level_traver_list or not len(level_traver_list):
        return None
    root = TreeNode(level_traver_list.pop(0))
    level = [root]
    while len(level_traver_list):
        tmp_level = []
        for node in level:

            if level_traver_list: # 防止访问溢出
                left = level_traver_list.pop(0)
                if left:
                    node.left = TreeNode(left)
            if level_traver_list:
                right = level_traver_list.pop(0)
                if right:
                    node.right = TreeNode(right)

            if node.left:
                tmp_level.append(node.left)
            if node.right:
                tmp_level.append(node.right)

        level = tmp_level

    return root
