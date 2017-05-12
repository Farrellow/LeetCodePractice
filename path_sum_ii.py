# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        def get_path(node, count, l, result):
            count += node.val
            l.append(node.val)
            if node.left:
                get_path(node.left, count, l, result)
                l.pop(-1)
                if node.right:
                    get_path(node.right, count, l, result)
                    l.pop(-1)
            else:
                if node.right:
                    get_path(node.right, count, l, result)
                    l.pop(-1)
                else:
                    if count == sum:
                        result.append([] + l)
        
        result = []
        get_path(root, 0, [], result)
        
        return result
    
    
