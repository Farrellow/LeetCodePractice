# -*- coding: utf-8 -*-

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        
        l = []
        temp = head
        while temp:
            l.append(temp)
            temp = temp.next
        result = l.pop(-1)
        temp = result
        while l:
            temp.next = l.pop(-1)
            temp = temp.next
            temp.next = None
        
        return result
        
