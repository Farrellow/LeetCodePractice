# -*- coding: utf-8 -*-

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = []
        for c in s:
            if c == '{':
                l.append(c)
            elif c == '[':
                l.append(c)
            elif c == '(':
                l.append(c)
            elif c == '}':
                if not l:
                    return False
                if l.pop() != '{':
                    return False
            elif c == ']':
                if not l:
                    return False
                if l.pop() != '[':
                    return False
            elif c == ')':
                if not l:
                    return False
                if l.pop() != '(':
                    return False
            else:
                return False
        if l:
            return False
        return True
