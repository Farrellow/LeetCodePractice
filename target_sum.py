# -*- coding: utf-8 -*-

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        target_d = {}
        target_d[nums[0]] = target_d.get(nums[0], 0) + 1
        target_d[-nums[0]] = target_d.get(-nums[0], 0) + 1
        for num in nums[1: ]:
            d = {}
            for k in target_d:
                d[k + num] = target_d.get(k, 0) + d.get(k + num, 0)
                d[k - num] = target_d.get(k, 0) + d.get(k - num, 0)
            target_d = d
        
        return target_d.get(S, 0)
