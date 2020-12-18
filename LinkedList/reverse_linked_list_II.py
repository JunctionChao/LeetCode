#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-09-24
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

# https://leetcode.com/problems/reverse-linked-list-ii/discuss/30666/Simple-Java-solution-with-clear-explanation

from link_list_fun import ListNode, generateNum, printListNode

def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    if not head:
        return head
    dummy = ListNode(0)
    dummy.next = head
    pre = dummy
    for _ in range(m - 1):
        pre = pre.next

    start = pre.next # a pointer to the beginning of a sub-list that will be reversed
    then = start.next # a pointer to a node that will be reversed

    # 1 - 2 -3 - 4 - 5 ; m=2; n =4 ---> pre = 1, start = 2, then = 3
    # dummy-> 1 -> 2 -> 3 -> 4 -> 5

    for _ in range(n - m):
        start.next = then.next
        then.next = pre.next
        pre.next = then
        then = start.next

    # first reversing : dummy->1 - 3 - 2 - 4 - 5; pre = 1, start = 2, then = 4
    # second reversing: dummy->1 - 4 - 3 - 2 - 5; pre = 1, start = 2, then = 5 (finish)

    return dummy.next


if __name__ == '__main__':
    ln = generateNum([5,4,3,2,1])
    printListNode(reverseBetween(ln, 2, 4))