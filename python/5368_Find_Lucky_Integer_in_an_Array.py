# -*- coding: utf-8 -*-

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        m = dict()
        for a in arr:
            m[a] = m.get(a, 0) + 1

        result = -1
        for k, v in m.items():
            if k == v:
                result = max(result, k)

        return result

