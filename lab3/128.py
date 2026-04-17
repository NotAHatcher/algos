class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        max_l = 0
        for i in s:
            if i-1 in s:
                pass
            else:
                k = i
                l = 1
                while k+1 in s:
                    l += 1
                    k += 1
                max_l = max(l,max_l)
        return max_l
a = Solution()
print(a.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))