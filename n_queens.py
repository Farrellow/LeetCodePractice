# -*- coding: utf-8 -*-

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if not n:
            return [[]]
        
        def get_config(l):
            result = []
            for i, j in l:
                s = '.' * j + 'Q' + '.' * (n - 1 - j)
                result.append(s)
            
            return result
        
        l = [(-1, -1) for _ in xrange(n)]
        result = []
        i = 0
        while True:
            _, k = l[i]
            k += 1
            flag = False
            for j in xrange(k, n):
                is_reuse = False
                for k in xrange(i):
                    x, y = l[k]
                    if j == y:
                        is_reuse = True
                        break
                    if i - x == j - y or i - x == y - j:
                        is_reuse = True
                        break
                if is_reuse:
                    continue
                else:
                    l[i] = (i, j)
                    flag = True
                    break
            if flag:
                if i == n - 1:
                    config = get_config(l)
                    result.append(config)
                else:
                    i += 1
            else:
                if i == 0:
                    break
                else:
                    l[i] = (-1, -1)
                    i -= 1
        
        return result
            
        
