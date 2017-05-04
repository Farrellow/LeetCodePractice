# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        def is_symmetric(a, b):
            if a.val != b.val:
                return False
            
            if a.left:
                if b.right:
                    if not is_symmetric(a.left, b.right):
                        return False
                else:
                    return False
            else:
                if b.right:
                    return False
            
            if a.right:
                if b.left:
                    if not is_symmetric(a.right, b.left):
                        return False
                else:
                    return False
            else:
                if b.left:
                    return False
            
            return True
        
        if root.left:
            if root.right:
                return is_symmetric(root.left, root.right)
            else:
                return False
        else:
            if root.right:
                return False
            else:
                return True
