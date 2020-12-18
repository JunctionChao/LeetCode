#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-23
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from link_list_fun import ListNode, generateNum, printListNode

def rotateRight(head: ListNode, k: int) -> ListNode:
    if not head or not head.next:
        return head

    fast = slow = head
    length = 1

    while fast.next:
        length += 1
        fast = fast.next

    rotateTimes = k % length

    if k == 0 or rotateTimes == 0:
        return head

    for _ in range(length - rotateTimes - 1):
        slow = slow.next

    temp = slow.next
    fast.next = head
    slow.next = None
    head = temp

    return head


if __name__ == '__main__':
    ln = generateNum([5,4,3,2,1])
    printListNode(rotateRight(ln, 2))