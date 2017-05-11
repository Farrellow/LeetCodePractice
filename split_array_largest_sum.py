# -*- coding: utf-8 -*-

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        if m == 1:
            return sum(nums)
        
        max_n = 0
        sum_n = 0
        for num in nums:
            max_n = max(max_n, num)
            sum_n += num
        
        def valid(mid):
            count = 0
            part = 0
            for num in nums:
                count += num
                if count > mid:
                    count = num
                    part += 1
                    if part >= m:
                        return False
                    else:
                        pass
                else:
                    pass
            
            return True
        
        left = max_n
        right = sum_n
        while left <= right:
            mid = (left + right) // 2
            if valid(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return right + 1
        
