from typing import Optional, List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.l = []
        self.backtrack(0, [])
        return self.l

    def backtrack(self, s, cur):
        self.l.append(cur[:])
        for i in range(s, len(self.nums)):
            cur.append(self.nums[i])
            self.backtrack(i + 1, cur)
            cur.pop()