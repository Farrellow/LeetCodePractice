# -*- coding: utf-8 -*-

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        zero = 0
        z_i = 0
        p = 1
        for i in xrange(length):
            if nums[i] == 0:
                if zero == 1:
                    return [0 for _ in xrange(length)]
                else:
                    zero = 1
                    z_i = i
            else:
                p *= nums[i]
        
        if zero:
            result = [0 for _ in xrange(length)]
            result[z_i] = p
        else:
            result = []
            for num in nums:
                result.append(p // num)
        return result
        
