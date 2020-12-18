#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-22
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from link_list_fun import ListNode, generateNum, printListNode

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    root = ml = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            ml.next = ListNode(l1.val)
            l1 = l1.next
        else:
            ml.next = ListNode(l2.val)
            l2 = l2.next
        ml = ml.next
    if l1:
        ml.next = l1
    if l2:
        ml.next = l2

    return root.next


def mergeTwoLists2(l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2
    if not l2:
        return l1

    if l1.val < l2.val:
        l1.next = mergeTwoLists2(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists2(l2.next, l1)
        return l2

def mergeTwoLists3(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 and l2:
        if l1.val > l2.val:
            l1, l2 = l2, l1
        l1.next = mergeTwoLists3(l1.next, l2)

    return l1 or l2



if __name__ == '__main__':
    l1 = generateNum([4, 2, 1])
    l2 = generateNum([4, 3, 1])

    ml = mergeTwoLists(l1, l2)
    printListNode(ml)