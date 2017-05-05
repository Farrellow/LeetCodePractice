# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        self.max_result = root.val
        self.d = {}  # node -> max path sum
        
        def find_max(node):
            result = node.val
            left_sum = 0
            if node.left:
                if self.d.get(node.left) == None:
                    find_max(node.left)
                left_sum = self.d[node.left]
            
            right_sum = 0
            if node.right:
                if self.d.get(node.right) == None:
                    find_max(node.right)
                right_sum = self.d[node.right]
            
            if left_sum >= 0:
                if right_sum >= 0:
                    result += left_sum + right_sum
                    self.d[node] = max(left_sum, right_sum) + node.val
                else:
                    result += left_sum
                    self.d[node] = result
            else:
                if right_sum >= 0:
                    result += right_sum
                    self.d[node] = result
                else:
                    result = max(result, left_sum, right_sum)
                    self.d[node] = node.val
            self.max_result = max(result, self.max_result)
        
        find_max(root)
        
        return self.max_result
        
