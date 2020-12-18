#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-11-27
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from link_list_fun import ListNode, generateNum, printListNode

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    if headA is None or headB is None:
        return None
    pa = headA
    pb = headB

    while pa is not pb:
        pa = headB if pa is None else pa.next
        pb = headA if pb is None else pb.next

    return pa