from typing import Optional, List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        pacific = [[0 for i in range(m)] for j in range(n)]
        atlantic = [[0 for i in range(m)] for j in range(n)]

        def dfs(i, j, cur):
            cur[i][j] = True
            for l in range(-1,2,2):
                if 0 <= i + l < n and not cur[i+l][j] and heights[i+l][j] >= heights[i][j]:
                    dfs(i+l, j, cur)
                if 0 <= j + l < m and not cur[i][j+l] and heights[i][j+l] >= heights[i][j]:
                    dfs(i, j+l, cur)

        for i in range(n):
            dfs(i, 0, pacific)
            dfs(i, m - 1, atlantic)
        for j in range(m):
            dfs(0, j, pacific)
            dfs(n - 1, j, atlantic)
        result = []
        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i, j])
        return result