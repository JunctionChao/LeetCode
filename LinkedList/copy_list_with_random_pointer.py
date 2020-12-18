#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-11-28
# Author  : Yuanbo Zhao (chaojunction@gmail.com)


# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


def copyRandomList(head: Node) -> Node:
    d = dict()
    m = n = head
    while m:
        d[m] = Node(m.val, None, None)
        m = m.next
    while n:
        d[n].next = d.get(n.next)
        d[n].random = d.get(n.random)
        n = n.next
    return d.get(head)


def copyRandomList2(head: Node) -> Node:
    d = collections.defaultdict(lambda: Node(0, None, None))
    d[None] = None
    n = head
    while n:
        d[n].val = n.val
        d[n].next = d[n.next]
        d[n].random = d[n.random]
        n = n.next
    return d[head]