#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-11-28
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from link_list_fun import ListNode, generateNum, printListNode

def middleNode(self, head: ListNode) -> ListNode:
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    return slow
