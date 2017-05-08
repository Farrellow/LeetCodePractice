# -*- coding: utf-8 -*-

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        result = 12 * 60
        h, m = timePoints[0].split(':')
        val = int(h) * 60 + int(m)
        root = TreeNode(val)
        
        def find_min(node, result, val):
            if val < node.val:
                result = min(result, node.val - val)
                if node.left:
                    result = min(result, find_min(node.left, result, val))
                else:
                    node.left = TreeNode(val)
            elif val > node.val:
                result = min(result, val - node.val)
                if node.right:
                    result = min(result, find_min(node.right, result, val))
                else:
                    node.right = TreeNode(val)
            else:
                return 0
            return result
        
        length = len(timePoints)
        for i in xrange(1, length):
            h, m = timePoints[i].split(':')
            val = int(h) * 60 + int(m)
            result = find_min(root, result, val)
            if result == 0:
                return 0
        
        left_node = root
        while left_node.left:
            left_node = left_node.left
        right_node = root
        while right_node.right:
            right_node = right_node.right
        result = min(result, 24 * 60 - right_node.val + left_node.val)
        
        return result
        
