from typing import Optional, List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        for a, b in prerequisites:
            adj[b].append(a)
        check = [0] * numCourses
        def dfs(cur):
            if check[cur] == 1:
                return False
            if check[cur] == 2:
                return True
            check[cur] = 1
            for neighbor in adj[cur]:
                if not dfs(neighbor):
                    return False
            check[cur] = 2
            return True
        for i in range(numCourses):
            if check[i] == 0:
                if not dfs(i):
                    return False
        return True