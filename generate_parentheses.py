# -*- coding: utf-8 -*-

class TreeNode(object):
    def __init__(self, s):
        self.s = s
        self.left = None
        self.right = None

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return []
        
        def build_tree(node, left, used):
            if n - used:
                node.left = TreeNode('(')
                build_tree(node.left, left + 1, used + 1)
            if left:
                node.right = TreeNode(')')
                build_tree(node.right, left - 1, used)
        
        root = TreeNode('(')
        build_tree(root, 1, 1)
        
        def get_result(node, s, result):
            s += node.s
            if node.left:
                if node.right:
                    get_result(node.left, s, result)
                    get_result(node.right, s, result)
                else:
                    get_result(node.left, s, result)
            else:
                if node.right:
                    get_result(node.right, s, result)
                else:
                    result.append(s)
        
        result = []
        get_result(root, '', result)
        
        return result
        
