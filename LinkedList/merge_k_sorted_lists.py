#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-22
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from link_list_fun import ListNode, generateNum, printListNode

def mergeKLists(lists: list([ListNode])) -> ListNode:
    res = []
    for l in lists:
        while l:
            res.append(l.val)
            l = l.next
    result = merge = ListNode(0)

    for i in sorted(res):
        merge.next = ListNode(i)
        merge = merge.next

    return result.next


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

def mergeKLists2(lists: list([ListNode])) -> ListNode:
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]
    mid = len(lists) // 2
    left = mergeKLists2(lists[:mid])
    right = mergeKLists2(lists[mid:])

    return mergeTwoLists(left, right)


if __name__ == '__main__':
    l1 = generateNum([5,4,1])
    l2 = generateNum([4,3,1])
    l3 = generateNum([6,2])
    printListNode(mergeKLists([l1, l2, l3]))