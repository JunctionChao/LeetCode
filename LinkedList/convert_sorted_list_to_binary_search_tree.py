#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-11-28
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

from link_list_fun import ListNode, generateNum, printListNode

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortedListToBST(head: ListNode) -> TreeNode:

    def toBST(head: ListNode, tail: ListNode) -> TreeNode:
        slow = fast = head
        if head is tail:
            return None
        while (fast is not tail and fast.next is not tail):
            fast = fast.next.next
            slow = slow.next
        root = TreeNode(slow.val)
        root.left = toBST(head, slow)
        root.right = toBST(slow.next, tail)
        return root

    if not head:
        return None
    return toBST(head, None)