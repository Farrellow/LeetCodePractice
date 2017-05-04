# coding; utf-8 -*-

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        length = len(nums)
        code = 1 << length
        for i in range(code):
            result = []
            j = 0
            while i:
                if i & 0b1:
                    result.append(nums[j])
                i >>= 1
                j += 1
            results.append(result)
        
        return results
