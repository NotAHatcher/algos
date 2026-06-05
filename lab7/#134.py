from typing import Optional, List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        cur = 0
        s = 0
        for i in range(len(gas)):
            d = gas[i] - cost[i]
            total += d
            cur += d
            if cur < 0:
                s = i + 1
                cur = 0
        return s if total >= 0 else -1