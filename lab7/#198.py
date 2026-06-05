from typing import Optional, List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            dp[i] = (max(dp[i-3],dp[i-2]) if i>1 else 0) + nums[i]
        return max(dp[-1],dp[-2])