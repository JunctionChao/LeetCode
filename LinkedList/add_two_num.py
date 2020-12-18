#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-16
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# https://leetcode.com/problems/add-two-numbers/solution/

"""
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0
    root = n = ListNode(0)
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        carry, val = divmod(carry, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next

# 根据数据生成链表
def generateNum(numList: list) -> ListNode:
    root = n = ListNode(0)
    while numList:
        x = numList.pop()
        ln = ListNode(x)
        n.next = ln
        n = n.next
    return root.next

# 打印链表
def printListNode(l: ListNode) -> None:
    while l:
        print(l.val, end='')
        l = l.next

if __name__ == '__main__':
    numList1 = [3, 4, 2]
    numList2 = [4, 6, 5]
    ln1 = generateNum(numList1)
    ln2 = generateNum(numList2)
    ln_result = addTwoNumbers(ln1, ln2)
    printListNode(ln_result)