# -*- coding: utf-8 -*-

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        length = len(preorder)
        if length != len(inorder):
            return None
        
        if not preorder:
            return None
        
        def build_tree(node, p_list, i_list):
            length = len(p_list)
            mid = p_list[0]
            node.val = mid
            if length == 1:
                pass
            else:
                for i in xrange(length):
                    if i_list[i] == mid:
                        i_left = i_list[0: i]
                        i_right = i_list[i + 1: length]
                        p_left = p_list[1: i + 1]
                        p_right = p_list[i + 1: length]
                        if i_left:
                            node.left = TreeNode(0)
                            build_tree(node.left, p_left, i_left)
                        if i_right:
                            node.right = TreeNode(0)
                            build_tree(node.right, p_right, i_right)
                        break
        
        root = TreeNode(0)
        build_tree(root, preorder, inorder)
        
        return root
        
