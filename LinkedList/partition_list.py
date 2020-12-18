#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-24
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from link_list_fun import ListNode, generateNum, printListNode

def partition(head: ListNode, x: int) -> ListNode:
    # separate the list into 2 distinct lists and link them afterwards.
    # p1, p2 traverses the list and hd1 and hd2 are the heads of two lists
    hd1 = p1 = ListNode(0)
    hd2 = p2 = ListNode(0)
    while head:
        if head.val < x:
            p1.next = head
            p1 = p1.next
        else:
            p2.next = head
            p2 = p2.next
        head = head.next

    p2.next = None
    p1.next = hd2.next
    return hd1.next


if __name__ == '__main__':
    ln = generateNum([2,5,2,3,4,1])
    printListNode(partition(ln, 3))