# -*- coding: utf-8 -*-


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = dict()
        for num in nums:
            if num in d:
                del d[num]
            else:
                d[num] = 1
        for k in d:
            return k

