#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-24
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from link_list_fun import ListNode, generateNum, printListNode

def reverseList(head: ListNode) -> ListNode:
    pre = None
    while head:
        cur = head
        head = head.next
        cur.next = pre
        pre = cur

    return pre

# 递归
def reverseListRecursive(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    new_head = reverseListRecursive(head.next)
    next_node = head.next
    next_node.next = head
    head.next = None

    return new_head


if __name__ == '__main__':
    ln = generateNum([5,4,3,2,1])
    printListNode(reverseList(ln))
