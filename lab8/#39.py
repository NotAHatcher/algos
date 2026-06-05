from typing import Optional, List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.l = []
        self.candidates = candidates
        self.backtrack(0, [], target)
        return self.l
    def backtrack(self, s, cur, target):
        if target == 0:
            self.l.append(cur[:])
            return
        if target < 0:
            return
        for i in range(s, len(self.candidates)):
            cur.append(self.candidates[i])
            self.backtrack(i, cur, target - self.candidates[i])
            cur.pop()