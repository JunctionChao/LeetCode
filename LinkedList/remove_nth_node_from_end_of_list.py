#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-21
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 根据数据生成链表 逆序生成链表
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

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next

    return head


if __name__ == '__main__':
    ln = generateNum([5, 4, 3, 2, 1])
    result = removeNthFromEnd(ln, 2)
    printListNode(result)