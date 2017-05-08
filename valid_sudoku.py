# -*- coding: utf-8 -*-

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        height = len(board)
        if height != 9:
            return False
        width = len(board[0])
        if width != 9:
            return False
        
        dl = [[[] for _ in xrange(3)] for _ in xrange(3)]
        for i in xrange(height):
            for j in xrange(width):
                dl[i // 3][j // 3].append((i, j))
        
        for i in xrange(height):
            for j in xrange(width):
                if board[i][j] != '.':
                    for x, y in dl[i // 3][j // 3]:
                        if x == i and y == j:
                            continue
                        if board[i][j] == board[x][y]:
                            return False
                    for k in xrange(height):
                        if k == i:
                            continue
                        if board[i][j] == board[k][j]:
                            return False
                    for l in xrange(width):
                        if l == j:
                            continue
                        if board[i][j] == board[i][l]:
                            return False
        
        return True
        
