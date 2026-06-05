from typing import Optional, List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        s = []
        for i in nums:
            left = 0
            right = len(s)
            while left < right:
                mid = (left + right) // 2
                if s[mid] < i:
                    left = mid + 1
                else:
                    right = mid
            if left == len(s):
                s.append(i)
            else:
                s[left] = i
        return len(s)