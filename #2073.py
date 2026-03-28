class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        s = len(tickets) * tickets[k] - (len(tickets)-(k+1))
        for i in range(len(tickets)):
            if tickets[i] < tickets[k]:
                if i>k:
                    s += 1
                s-=(tickets[k] - tickets[i])
        return s