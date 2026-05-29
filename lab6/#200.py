from typing import Optional, List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.n = len(grid)
        self.m = len(grid[0])
        s = 0
        self.grid = grid
        for i in range(self.n):
            for j in range(self.m):
                s += self.check(i, j)
        return s

    def check(self, i, j):
        if self.grid[i][j] == '0':
            return 0
        else:
            self.grid[i][j] = '0'
            for l in range(-1, 2, 2):
                if i + l >= 0 and i + l < self.n:
                    self.check(i + l, j)
                if j + l >= 0 and j + l < self.m:
                    self.check(i, j + l)
            return 1
