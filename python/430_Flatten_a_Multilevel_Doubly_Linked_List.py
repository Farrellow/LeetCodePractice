# -*- coding: utf-8 -*-

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        def _merge_node(a_node, b_node):
            a_node.next = b_node
            b_node.prev = a_node

            tail_node = b_node
            while tail_node.next is not None:
                tail_node = tail_node.next

            return tail_node

        def _flatten_a_line(node):
            flatten_node = Node(node.val, None, None, None)
            if node.child is not None:
                child_node = _flatten_a_line(node.child)
                tail_node = _merge_node(flatten_node, child_node)
            else:
                tail_node = flatten_node

            temp = node.next
            while temp is not None:
                new_node = Node(temp.val, None, None, None)
                tail_node = _merge_node(tail_node, new_node)
                if temp.child is not None:
                    child_node = _flatten_a_line(temp.child)
                    tail_node = _merge_node(tail_node, child_node)
                temp = temp.next

            return flatten_node

        root = _flatten_a_line(head)

        return root

