# -*- coding: utf-8 -*-

class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.not_used = True
    
    def get_neighbor(self, w, h):
        result = []
        if self.x < h - 1:
            result.append((self.x + 1, self.y))
        if self.x > 0:
            result.append((self.x - 1, self.y))
        if self.y < w - 1:
            result.append((self.x, self.y + 1))
        if self.y > 0:
            result.append((self.x, self.y - 1))
        
        return result

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        h = len(board)
        if not h:
            return
        w = len(board[0])
        if not w:
            return
        if h < 3 or w < 3:
            return
        
        l = [Vector(x, y) for x in range(h) for y in range(w)]
        buff = []
        stack = []
        for i in range(h):
            for j in range(w):
                if board[i][j] == 'O' and l[i * w + j].not_used:
                    if i == 0 or i == h - 1 or j == 0 or j == w - 1:
                        is_alive = True
                    else:
                        is_alive = False
                    buff = []
                    stack = []
                    v = l[i * w + j]
                    v.not_used = False
                    buff.append((i, j))
                    stack.append(v)
                    while stack:
                        v = stack[-1]
                        neighbors = v.get_neighbor(w, h)
                        has_neighbor = False
                        for x, y in neighbors:
                            if board[x][y] == 'O' and l[x * w + y].not_used:
                                if x == 0 or x == h - 1 or y == 0 or y == w - 1:
                                    is_alive = True
                                v = l[x * w + y]
                                v.not_used = False
                                buff.append((x, y))
                                stack.append(v)
                                has_neighbor = True
                        if has_neighbor:
                            pass
                        else:
                            stack.pop(-1)
                    if not is_alive:
                        for x, y in buff:
                            board[x][y] = 'X'
