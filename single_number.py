# coding: utf-8 -*-

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for num in nums:
            if d.get(num):
                d[num] += 1
            else:
                d[num] = 1
        
        for k, v in d.items():
            if v == 1:
                return k
