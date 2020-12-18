#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-23
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from link_list_fun import ListNode, generateNum, printListNode

def deleteDuplicates(head: ListNode) -> ListNode:
    dummy = pre = ListNode(0)
    dummy.next = head

    while head and head.next:
        if head.val == head.next.val:
            while head and head.next and head.val == head.next.val:
                head = head.next
            head = head.next
            pre.next = head
        else:
            head = head.next
            pre = pre.next

    return dummy.next


if __name__ == '__main__':
    ln = generateNum([5,4,4,3,3,2,1])
    printListNode(deleteDuplicates(ln))

