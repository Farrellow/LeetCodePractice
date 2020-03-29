# -*- coding: utf-8 -*-

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        length = len(rating)
        result = 0
        for i in range(1, length - 1):
            r = rating[i]
            left_lt = 0
            left_gt = 0
            right_lt = 0
            right_gt = 0
            for j in range(i):
                if rating[j] < r:
                    left_lt += 1
                else:
                    left_gt += 1
            for k in range(i + 1, length):
                if rating[k] < r:
                    right_lt += 1
                else:
                    right_gt += 1
            result += (left_lt * right_gt) + (left_gt * right_lt)

        return result

