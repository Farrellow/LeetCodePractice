# -*- coding: utf-8 -*-

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = s.strip().split()
        l.reverse()
        if not l:
            return ''
        
        result = ''
        for i in l:
            result += i + ' '
        
        return result[: -1]
        
