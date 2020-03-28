# -*- coding: utf-8 -*-

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def _get_perimeter(i, j, h, w):
            _perimeter = 4
            if i > 0:
                if grid[i - 1][j] == 1:
                    _perimeter -= 1
            if i < h - 1:
                if grid[i + 1][j] == 1:
                    _perimeter -= 1
            if j > 0:
                if grid[i][j - 1] == 1:
                    _perimeter -= 1
            if j < w - 1:
                if grid[i][j + 1] == 1:
                    _perimeter -= 1

            return _perimeter

        perimeter = 0
        highth = len(grid)
        width = len(grid[0])
        for i in range(highth):
            for j in range(width):
                if grid[i][j] == 1:
                    p = _get_perimeter(i, j, highth, width)
                    perimeter += p
                else:
                    continue

        return perimeter

