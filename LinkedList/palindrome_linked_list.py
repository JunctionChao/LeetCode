#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-11-28
# Author  : Yuanbo Zhao (chaojunction@gmail.com)

from link_list_fun import ListNode, generateNum, printListNode

# in O(n) time and O(1) space
def isPalindrome(head: ListNode) -> bool:
    # rev records the first half, need to set the same structure as fast, slow, hence later we have rev.next
    rev = None
    # initially slow and fast are the same, starting from head
    slow = fast = head
    while fast and fast.next:
        # fast traverses faster and moves to the end of the list if the length is odd
        fast = fast.next.next
        
        # take it as a tuple being assigned (rev, rev.next, slow) = (slow, rev, slow.next), hence the re-assignment of slow would not affect rev (rev = slow)
        rev, rev.next, slow = slow, rev, slow.next
    if fast: # 表明是奇数
       # fast is at the end, move slow one step further for comparison(cross middle one)
        slow = slow.next
    # compare the reversed first half with the second half
    while rev and rev.val == slow.val:
        slow = slow.next
        rev = rev.next
    
    # if equivalent then rev become None, return True; otherwise return False 
    return not rev