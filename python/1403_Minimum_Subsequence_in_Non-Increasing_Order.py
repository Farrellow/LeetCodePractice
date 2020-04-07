# -*- coding: utf-8 -*-


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums, reverse=True)
        sums = sum(nums)
        result = list()
        result_sums = 0
        for num in sorted_nums:
            if result_sums > sums:
                break
            result_sums += num
            sums -= num
            result.append(num)

        return result
