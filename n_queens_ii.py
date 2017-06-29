# -*- coding: utf-8 -*-

class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        l = [(-1, -1) for _ in xrange(n)]
        i = 0
        while True:
            _, j = l[i]
            j += 1
            flag = False
            for k in xrange(j, n):
                is_used = False
                for x, y in l[: i]:
                    if y == k:
                        is_used = True
                        break
                    if i - x == k - y or i - x == y - k:
                        is_used = True
                        break
                if is_used:
                    continue
                else:
                    l[i] = (i, k)
                    flag = True
                    break
            if flag:
                if i == n - 1:
                    result += 1
                else:
                    i += 1
            else:
                if i == 0:
                    break
                else:
                    l[i] = (-1, -1)
                    i -= 1
        
        return result
        
