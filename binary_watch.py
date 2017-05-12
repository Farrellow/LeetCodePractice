# -*- coding: utf-8 -*-

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        def get_all(n, m, bit, l):
            if n:
                bit <<= 1
                if n == m:
                    bit |= 1
                    get_all(n - 1, m - 1, bit, l)
                else:
                    get_all(n, m - 1, bit, l)
                    bit |= 1
                    get_all(n - 1, m - 1, bit, l)
            else:
                if n == m:
                    l.append(bit)
                else:
                    l.append(bit << m)
        
        l = []
        get_all(num, 10, 0b0, l)
        result = []
        for i in l:
            h = i >> 6
            if h > 11:
                continue
            m = i & 0b111111
            if m > 59:
                continue
            result.append('%d:%.2d' % (h, m))
        
        return result
        
