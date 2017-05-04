# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next
        cnt = length - (k % length) - 1
        temp = head
        while cnt:
            temp = temp.next
            cnt -= 1
        if temp.next:
            tail = temp.next
            while tail.next:
                tail = tail.next
            tail.next = head
            result = temp.next
            temp.next  = None
            return result
        else:
            return head
