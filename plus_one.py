# -*- coding: utf-8 -*-

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = 0
        for d in digits:
            n *= 10
            n += d
        result = []
        n += 1
        while n:
            result.insert(0, n % 10)
            n //= 10
        
        return result
        
