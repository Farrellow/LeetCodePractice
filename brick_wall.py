# -*- coding: utf-8 -*-

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        length = len(wall)
        max_n = 0
        d = {}
        sum_n = sum(wall[0])
        for line in wall:
            count = 0
            for i in line:
                count += i
                if count == sum_n:
                    continue
                if d.get(count) == None:
                    d[count] = 1
                else:
                    d[count] += 1
                max_n = max(max_n, d[count])
        
        return length - max_n
        
