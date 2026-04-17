class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        ans = range(1, max(piles)+1)
        l = 0
        r = len(ans) - 1
        while l <= r:
            mid = (l+r)//2
            c = 0
            k = ans[mid]
            for i in piles:
                c += i//k + (i%k > 0)
            if c > h:
                l = mid + 1
            else:
                r = mid - 1
                s = k
        return s

a  = Solution()
print(a.minEatingSpeed(piles = [3,6,7,11], h = 8))