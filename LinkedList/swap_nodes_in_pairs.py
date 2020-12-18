#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-23
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from link_list_fun import ListNode, generateNum, printListNode

def swapPairs(head: ListNode) -> ListNode:
    pre = ListNode(0)
    pre.next = head

    slow = pre
    if pre.next:
        fast = pre.next.next
    else:
        fast = None

    while slow and fast:
        post = fast.next
        fast.next = slow.next
        slow.next = fast
        fast.next.next = post

        slow = slow.next.next
        if post:
            fast = post.next
        else:
            break

    return pre.next


if __name__ == '__main__':
    ln = generateNum([4,3,2,1])
    printListNode(swapPairs(ln))