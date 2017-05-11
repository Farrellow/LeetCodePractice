# -*- coding: utf-8 -*-

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def get_bit_len(a):
            result = []
            while a:
                result.append(a & 1)
                a >>= 1
            
            return result
        
        ml = get_bit_len(m)
        nl = get_bit_len(n)
        if len(ml) != len(nl):
            return 0
        
        result = 0
        for i in xrange(len(ml) - 1, -1, -1):
            if ml[i] == nl[i]:
                result <<= 1
                result |= ml[i]
            else:
                result <<= (i + 1)
                break
        
        return result
        
