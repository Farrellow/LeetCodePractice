# -*- coding: utf-8 -*-

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        if numRows == 0:
            return s
        length = len(s)
        result = ''
        for i in range(numRows):
            if i == 0 or i == numRows - 1:
                j = i
                while j < length:
                    result += s[j]
                    j += (numRows - 1) * 2
            else:
                j = i
                while j < length:
                    result += s[j]
                    j += (numRows - 1 - i) * 2
                    if j < length:
                        result += s[j]
                        j += i * 2
                    else:
                        break
        
        return result
