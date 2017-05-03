# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        
        def get_i(l):
            i = 0
            temp = l
            while temp:
                i *= 10
                i += temp.val
                temp = temp.next
            return i
        
        i1 = get_i(l1)
        i2 = get_i(l2)
        
        def get_list(i):
            if i // 10:
                node = ListNode(i % 10)
                head, tail = get_list(i // 10)
                tail.next = node
                return head, node
            else:
                node = ListNode(i)
                return node, node
        
        i = i1 + i2
        head, _ = get_list(i)
        return head
        
