# -*- coding: utf-8 -*-

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        height = len(board)
        if height != 9:
            return False
        width = len(board[0])
        if width != 9:
            return False
        
        l = []
        dl = [[[] for _ in xrange(3)] for _ in xrange(3)]
        for i in xrange(height):
            for j in xrange(width):
                if board[i][j] == '.':
                    l.append((i, j))
                dl[i // 3][j // 3].append((i, j))
        
        length = len(l)
        k = 0
        while True:
            i, j = l[k]
            flag = False
            if board[i][j] == '.':
                start = 1
            else:
                start = int(board[i][j])
            for n in xrange(start, 10):
                flag0 = False
                for x, y in dl[i // 3][j // 3]:
                    if str(n) == board[x][y]:
                        flag0 = True
                        break
                if flag0:
                    continue
                if str(n) in board[i]:
                    continue
                flag1 = False
                for m in xrange(height):
                    if str(n) == board[m][j]:
                        flag1 = True
                        break
                if flag1:
                    continue
                flag = True
                board[i][j] = str(n)
                break
            if flag:
                if k == length - 1:
                    return
                else:
                    k += 1
            else:
                if k == 0:
                    return
                else:
                    board[i][j] = '.'
                    k -= 1
        
