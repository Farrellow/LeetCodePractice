# -*- coding: utf-8 -*-

class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = [-1 for _ in xrange(n)]
        max_n = ((n + 1) * n) // 2
        
        def get_amount(start, end, l):
            if end - start == 0:
                return 0
            elif end - start == 1:
                return start
            elif end - start == 2:
                return start + 1
            elif end - start == 3:
                return start + end - 1
            else:
                if l[end - start] != -1:
                    mid = start + l[end - start]
                    return mid + max(get_amount(start, mid - 1, l), get_amount(mid + 1, end, l))
                result = max_n
                for mid in xrange(start + 1, end):
                    a = mid + max(get_amount(start, mid - 1, l), get_amount(mid + 1, end, l))
                    if a < result:
                        result = a
                        l[end - start] = mid - start
                return result
        
        return get_amount(1, n, l)
        
