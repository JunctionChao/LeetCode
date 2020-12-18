#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-11-28
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# https://leetcode.com/problems/linked-list-cycle-ii/discuss/44783/Share-my-python-solution-with-detailed-explanation
from link_list_fun import ListNode, generateNum, printListNode

def detectCycle(head: ListNode) -> ListNode:
    try:
        slow = head.next
        fast = head.next.next
        while fast is not slow:
            fast = fast.next.next
            slow = slow.next
    except:
        return None

    while head is not slow:
        head = head.next
        slow = slow.next

    return head
