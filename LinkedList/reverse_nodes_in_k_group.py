#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-23
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from link_list_fun import ListNode, generateNum, printListNode

# 递归
def reverseKGroup(head: ListNode, k: int) -> ListNode:
    curr = head
    count = 0
    while curr and count < k:
        curr = curr.next
        count += 1
    if count == k:
        curr = reverseKGroup(curr, k)

        while count > 0:
            tmp = head.next
            head.next = curr
            curr = head
            head = tmp

            count -= 1

        head = curr

    return head



if __name__ == '__main__':
    ln = generateNum([5,4,3,2,1])
    printListNode(reverseKGroup(ln, 2))