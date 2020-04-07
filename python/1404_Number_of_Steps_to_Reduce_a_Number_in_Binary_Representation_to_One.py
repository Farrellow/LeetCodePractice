# -*- coding: utf-8 -*-


class Solution:
    def numSteps(self, s: str) -> int:
        length = len(s)
        s_i = 0
        for i in range(length):
            s_i += int(s[i]) * (2 ** (length - 1 - i))

        result = 0
        while s_i != 1:
            if s_i % 2:
                s_i += 1
            else:
                s_i >>= 1
            result += 1

        return result
