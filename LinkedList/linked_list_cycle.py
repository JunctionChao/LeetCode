#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-11-27
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from link_list_fun import ListNode, generateNum, printListNode

# 定义两个指针，同时从链表的头节点出发，一个指针一次走一步，另一个指针一次走两步。
# 如果走得快的指针追上了走得慢的指针，那么链表就是环形链表；
# 如果走得快的指针走到了链表的末尾（next指向 NULL）都没有追上第一个指针，那么链表就不是环形链表

def hasCycle(head: ListNode) -> bool:
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False


def hasCycle2(head: ListNode) -> bool:
    walker = head
    runner = head
    while (runner is not None and runner.next is not None):
        walker = walker.next
        runner = runner.next.next
        if walker is runner:
            return True
    return False

