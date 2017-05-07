# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def is_sub_tree(s_node, t_node):
            result = True
            if s_node.left:
                if t_node.left:
                    if s_node.left.val == t_node.left.val:
                        result = result and is_sub_tree(s_node.left, t_node.left)
                        if not result:
                            return result
                    else:
                        return False
                else:
                    return False
            else:
                if t_node.left:
                    return False
                else:
                    pass
            
            if s_node.right:
                if t_node.right:
                    if s_node.right.val == t_node.right.val:
                        result = result and is_sub_tree(s_node.right, t_node.right)
                        if not result:
                            return result
                    else:
                        return False
                else:
                    return False
            else:
                if t_node.right:
                    return False
                else:
                    pass
            
            return result
        
        def find_sub_tree(node, val, t):
            if node.val == val:
                result = is_sub_tree(node, t)
                if result:
                    return result
                else:
                    pass
            else:
                pass
            
            if node.left:
                result = find_sub_tree(node.left, val, t)
                if result:
                    return result
                else:
                    pass
            else:
                pass
            
            if node.right:
                result = find_sub_tree(node.right, val, t)
                if result:
                    return result
            
            return False
        
        return find_sub_tree(s, t.val, t)
            
