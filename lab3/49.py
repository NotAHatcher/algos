class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dist = {}
        for i in strs:
            a = ''.join(sorted(i))
            if a in dist:
                dist[a].append(i)
            else:
                dist[a] = [i]
        return list(dist.values())

a = Solution()
print(a.groupAnagrams([""]))