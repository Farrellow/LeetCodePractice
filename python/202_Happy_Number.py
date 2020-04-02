# -*- coding: utf-8 -*-


class Solution:
    def isHappy(self, n: int) -> bool:
        def _next(_n):
            r = 0
            while _n:
                a = _n % 10
                r += (a ** 2)
                _n //= 10
            return r

        nums_set = set()
        while n not in nums_set:
            nums_set.add(n)
            n = _next(n)

        return n == 1

