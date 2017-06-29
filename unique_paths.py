# -*- coding: utf-8 -*-

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        mem = [[0 for _ in xrange(n)] for _ in xrange(m)]
        mem[0][0] = 1
        
        for i in xrange(m):
            for j in xrange(n):
                if i != m - 1:
                    mem[i + 1][j] += mem[i][j]
                if j != n - 1:
                    mem[i][j + 1] += mem[i][j]
        
        return mem[m - 1][n - 1]
        
