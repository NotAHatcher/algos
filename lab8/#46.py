from typing import Optional, List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.l = []
        self.nums = nums
        self.used = [False] * len(nums)
        self.backtrack([])
        return self.l

    def backtrack(self, cur):
        if len(cur) == len(self.nums):
            self.l.append(cur[:])
            return
        for i in range(len(self.nums)):
            if not self.used[i]:
                self.used[i] = True
                cur.append(self.nums[i])
                self.backtrack(cur)
                cur.pop()
                self.used[i] = False
