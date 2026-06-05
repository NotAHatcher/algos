from typing import Optional, List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board
        self.word = word
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] == word[0] and self.dfs(r, c, 0):
                    return True
        return False

    def dfs(self, r, c, index):
        if index == len(self.word):
            return True
        if (r < 0 or r >= self.rows or c < 0 or c >= self.cols or
                self.board[r][c] != self.word[index]):
            return False
        temp = self.board[r][c]
        self.board[r][c] = 1
        f = (self.dfs(r + 1, c, index + 1) or
             self.dfs(r - 1, c, index + 1) or
             self.dfs(r, c + 1, index + 1) or
             self.dfs(r, c - 1, index + 1))
        self.board[r][c] = temp
        return f
