class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        dist = {}
        for i in nums:
            if i in dist:
                dist[i] += 1
            else:
                dist[i] = 1
        c = [[] for i in range(len(nums))]
        for i in dist:
            c[dist[i]-1].append(i)
        j = -1
        ans = []
        while k > 0:
            if k > len(c[j]):
                k -= len(c[j])
                ans = ans + c[j]
                j -= 1
            else:
                ans = ans + c[j][:k]
                k = 0
        return ans

a = Solution()
print(a.topKFrequent(nums = [1,2,1,2,1,2,3,1,3,2], k = 2))