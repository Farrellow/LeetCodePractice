# -*- coding: utf-8 -*-

class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x + y < z:
            return False
        if x == 0 or y == 0:
            if x == z or y == z or x + y == z:
                return True
            else:
                return False
                
        if x > y:
            m, n = x, y
        else:
            m, n = y, x
        
        a = m % n
        while a:
            if a == 1:
                return True
            n = a
            a = m % n
        
        if (z - m) % n:
            return False
        else:
            return True
